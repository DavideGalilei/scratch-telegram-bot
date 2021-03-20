import asyncio

from pyrogram import Client, filters
from quart import Quart, make_response, jsonify, request


app = Quart(__name__)

bot = Client(
    ":memory:",
    api_id=0,
    api_hash="",
    bot_token="",
)

queue = asyncio.Queue()


async def aeval(code):
    exec(f"async def __ex():\n    return {code}")
    return await locals()["__ex"]()


@bot.on_message(
    filters.text
    & (filters.private | (filters.group & ~filters.linked_channel))
)
async def handler(bot, msg):
    await queue.put(msg)


@app.route("/translate")
async def route():
    text = request.args["text"]

    try:
        if text in ("update", "ping"):
            if queue.empty():
                result = ""
            else:
                result = await queue.get()
                result = "\n|".join(
                    map(str, (result.chat.id, result.from_user.first_name, result.text))
                )
        else:
            result = str(await aeval(text))
    except Exception as e:
        result = f"{type(e).__name__}\n|{type(e)}\n|{e}"

    resp = await make_response(jsonify({"result": result}))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


if __name__ == "__main__":
    bot.start()
    app.run(loop=asyncio.get_event_loop())
