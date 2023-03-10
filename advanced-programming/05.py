import asyncio


class BatchFetcher:
    # The `database` has an `async_fetch` method
    # that you should use in your code. This method
    # takes in a record id and returns a record.
    def __init__(self, database):
        self.database = database

    async def fetch_records(self, record_ids):
        result = []
        for record_id in record_ids:
            el = self.database.async_fetch(record_id)
            result.append(el)
        return await asyncio.gather(*result)
