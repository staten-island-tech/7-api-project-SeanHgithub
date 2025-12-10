import requests
import asyncio
import fortnite_api

async def main():
    async with fortnite_api.Client(api_key="50ae7ff9-459e-4dbc-b8f2-b6d56e19062c") as client:
        stats = await client.fetch_br_stats(name="Ship")
        print(stats)

if __name__ == "__main__":
    asyncio.run(main())

