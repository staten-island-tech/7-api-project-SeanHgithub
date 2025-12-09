import requests
import asyncio
import fortnite_api

async def main():
   async with fortnite_api.Client(api_key="your_api_key"):
      stats = await client.fetch_br_stats(name='some_username')
      print(stats)

if __name__ == "__main__":
   asyncio.run(main())
