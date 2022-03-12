import asyncio
from typing import List

import requests


def download_images(sorted_urls) -> List:
    """Download images and convert to list of PIL images

    Once in an array of PIL.images we can easily convert this to a PDF.

    :param sorted_urls: List of sorted URLs for split financial disclosure
    :return: image_list
    """

    async def main(urls):
        image_list = []
        loop = asyncio.get_event_loop()
        futures = [loop.run_in_executor(None, requests.get, url) for url in urls]
        for response in await asyncio.gather(*futures):
            image_list.append(response.content)
        return image_list

    loop = asyncio.get_event_loop()
    image_list = loop.run_until_complete(main(sorted_urls))

    return image_list
