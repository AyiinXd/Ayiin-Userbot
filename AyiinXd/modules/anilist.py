"""
Anilist Search Plugin for Userbot
Usage : .anilist animeName
By :- @Zero_cool7870
ported char, airing and manga by @sandy1709 and @mrconfused
"""

import json
import re

import requests

from AyiinXd import Ayiin
from AyiinXd.ayiin import ayiin_cmd, time_formatter


def shorten(description, info="anilist.co"):
    msg = ""
    if len(description) > 700:
        description = f"{description[:200]}....."
        msg += f"\n**Description**:\n{description} [Read More]({info})"
    else:
        msg += f"\n**Description**: \n   {description}"
    return (
        msg.replace("<br>", "")
        .replace("</br>", "")
        .replace("<i>", "")
        .replace("</i>", "")
        .replace("__", "**")
    )


character_query = """
    query ($query: String) {
        Character (search: $query) {
               id
               name {
                     first
                     last
                     full
               }
               siteUrl
               image {
                        large
               }
               description
        }
    }
"""

airing_query = """
    query ($id: Int,$search: String) {
      Media (id: $id, type: ANIME,search: $search) {
        id
        episodes
        title {
          romaji
          english
          native
        }
        nextAiringEpisode {
           airingAt
           timeUntilAiring
           episode
        }
      }
    }
    """

anime_query = """
   query ($id: Int,$search: String) {
      Media (id: $id, type: ANIME,search: $search) {
        id
        title {
          romaji
          english
          native
        }
        description (asHtml: false)
        startDate{
            year
          }
          episodes
          season
          type
          format
          status
          duration
          siteUrl
          studios{
              nodes{
                   name
              }
          }
          trailer{
               id
               site
               thumbnail
          }
          averageScore
          genres
          bannerImage
      }
    }
"""

manga_query = """
query ($id: Int,$search: String) {
      Media (id: $id, type: MANGA,search: $search) {
        id
        title {
          romaji
          english
          native
        }
        description (asHtml: false)
        startDate{
            year
          }
          type
          format
          status
          siteUrl
          averageScore
          genres
          bannerImage
      }
    }
"""


async def callAPI(search_str):
    query = """
    query ($id: Int,$search: String) {
      Media (id: $id, type: ANIME,search: $search) {
        id
        title {
          romaji
          english
        }
        description (asHtml: false)
        startDate{
            year
          }
          episodes
          chapters
          volumes
          season
          type
          format
          status
          duration
          averageScore
          genres
          bannerImage
      }
    }
    """
    variables = {"search": search_str}
    url = "https://graphql.anilist.co"
    response = requests.post(
        url,
        json={
            "query": query,
            "variables": variables})
    return response.text


async def formatJSON(outData):
    msg = ""
    jsonData = json.loads(outData)
    res = list(jsonData.keys())
    if "errors" in res:
        msg += f"**Error** : `{jsonData['errors'][0]['message']}`"
        return msg
    jsonData = jsonData["data"]["Media"]
    if "bannerImage" in jsonData.keys():
        msg += f"[〽️]({jsonData['bannerImage']})"
    else:
        msg += "〽️"
    title = jsonData["title"]["romaji"]
    link = f"https://anilist.co/anime/{jsonData['id']}"
    msg += f"[{title}]({link})"
    msg += f"\n\n**Type** : {jsonData['format']}"
    msg += "\n**Genres** : "
    for g in jsonData["genres"]:
        msg += f"{g} "
    msg += f"\n**Status** : {jsonData['status']}"
    msg += f"\n**Episode** : {jsonData['episodes']}"
    msg += f"\n**Year** : {jsonData['startDate']['year']}"
    msg += f"\n**Score** : {jsonData['averageScore']}"
    msg += f"\n**Duration** : {jsonData['duration']} min\n\n"
    # https://t.me/catuserbot_support/19496
    cat = f"{jsonData['description']}"
    msg += " __" + re.sub("<br>", "\n", cat) + "__"
    return msg


url = "https://graphql.anilist.co"


@ayiin_cmd(pattern=r"anichar ?(.*)")
async def anichar(event):
    search = event.pattern_match.group(1)
    reply_to_id = event.reply_to_msg_id or event.message.id
    variables = {"query": search}
    if json := (
        requests.post(
            url,
            json={
            "query": character_query,
            "variables": variables}) .json()["data"] .get(
                "Character",
            None)):
        msg = f"**{json.get('name').get('full')}**\n"
        description = f"{json['description']}"
        site_url = json.get("siteUrl")
        msg += shorten(description, site_url)
        if image := json.get("image", None):
            image = image.get("large")
            await event.delete()
            await Ayiin.send_file(
                event.chat_id, image, caption=msg, parse_mode="md", reply_to=reply_to_id
            )
        else:
            await event.edit(msg)
    else:
        await event.edit("Sorry, No such results")


@ayiin_cmd(pattern="airing ?(.*)")
async def arings(event):
    search = event.pattern_match.group(1)
    variables = {"search": search}
    response = requests.post(
        url, json={"query": airing_query, "variables": variables}
    ).json()["data"]["Media"]
    ms_g = f"**Name**: **{response['title']['romaji']}**(`{response['title']['native']}`)\n**ID**: `{response['id']}`"
    if response["nextAiringEpisode"]:
        airing_time = response["nextAiringEpisode"]["timeUntilAiring"] * 1000
        airing_time_final = time_formatter(airing_time)
        ms_g += f"\n**Episode**: `{response['nextAiringEpisode']['episode']}`\n**Airing In**: `{airing_time_final}`"
    else:
        ms_g += f"\n**Episode**:{response['episodes']}\n**Status**: `N/A`"
    await event.edit(ms_g)


@ayiin_cmd(pattern="animanga ?(.*)")
async def animanga(event):
    search = event.pattern_match.group(1)
    reply_to_id = event.reply_to_msg_id or event.message.id
    variables = {"search": search}
    json = (
        requests.post(url, json={"query": manga_query, "variables": variables})
        .json()["data"]
        .get("Media", None)
    )
    ms_g = ""
    if json:
        title, title_native = json["title"].get(
            "romaji", False), json["title"].get(
            "native", False)
        start_date, status, score = (
            json["startDate"].get("year", False),
            json.get("status", False),
            json.get("averageScore", False),
        )
        if title:
            ms_g += f"**{title}**"
            if title_native:
                ms_g += f"(`{title_native}`)"
        if start_date:
            ms_g += f"\n**Start Date** - `{start_date}`"
        if status:
            ms_g += f"\n**Status** - `{status}`"
        if score:
            ms_g += f"\n**Score** - `{score}`"
        ms_g += "\n**Genres** - "
        for x in json.get("genres", []):
            ms_g += f"{x}, "
        ms_g = ms_g[:-2]
        image = json.get("bannerImage", False)
        ms_g += f"_{json.get('description', None)}_"
        ms_g = (
            ms_g.replace("<br>", "")
            .replace("</br>", "")
            .replace("<i>", "")
            .replace("</i>", "")
        )
        if image:
            try:
                await Ayiin.send_file(
                    event.chat_id,
                    image,
                    caption=ms_g,
                    parse_mode="md",
                    reply_to=reply_to_id,
                )
                await event.delete()
            except BaseException:
                ms_g += f" [〽️]({image})"
                await event.edit(ms_g)
        else:
            await event.edit(ms_g)


@ayiin_cmd(pattern="anilist ?(.*)")
async def anilist(event):
    input_str = event.pattern_match.group(1)
    event = await event.edit("Searching...")
    result = await callAPI(input_str)
    msg = await formatJSON(result)
    await event.edit(msg, link_preview=True)
