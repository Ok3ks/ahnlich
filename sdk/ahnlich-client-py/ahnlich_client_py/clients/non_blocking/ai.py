import typing

from ahnlich_client_py.builders import AsyncAhnlichAIRequestBuilder
from ahnlich_client_py.config import AhnlichPoolSettings
from ahnlich_client_py.internals import ai_query, ai_response
from ahnlich_client_py.internals import serde_types as st
from ahnlich_client_py.internals.async_base_client import BaseClient


class AhnlichAIClient(BaseClient):
    """Async Wrapper for interacting with Ahnlich AI Proxy"""

    def __init__(
        self,
        address: str,
        port: int,
        connect_timeout_sec: float = 5.0,
        pool_settings: AhnlichPoolSettings = AhnlichPoolSettings(),
    ) -> None:
        super().__init__(
            address=address,
            port=port,
            connect_timeout_sec=connect_timeout_sec,
            pool_settings=pool_settings,
        )

    def get_response_class(self):
        return ai_response.AIServerResult

    async def create_store(
        self,
        store_name: str,
        query_model: ai_query.AIModel = ai_query.AIModel__AllMiniLML6V2,
        index_model: ai_query.AIModel = ai_query.AIModel__AllMiniLML6V2,
        predicates: typing.Sequence[str] = None,
        non_linear_indices: typing.Sequence[ai_query.NonLinearAlgorithm] = None,
        error_if_exists: bool = True,
        tracing_id: typing.Optional[str] = None,
    ):
        builder = AsyncAhnlichAIRequestBuilder(tracing_id)
        builder.create_store(
            store_name=store_name,
            query_model=query_model,
            index_model=index_model,
            predicates=predicates,
            non_linear_indices=non_linear_indices,
            error_if_exists=error_if_exists,
        )
        return await self.process_request(builder.to_server_query())

    async def get_pred(
        self,
        store_name: str,
        condition: ai_query.PredicateCondition,
        tracing_id: typing.Optional[str] = None,
    ):
        builder = AsyncAhnlichAIRequestBuilder(tracing_id)
        builder.get_pred(store_name=store_name, condition=condition)
        return await self.process_request(builder.to_server_query())

    async def get_sim_n(
        self,
        store_name: str,
        search_input: ai_query.StoreInput,
        closest_n: st.uint64 = 1,
        algorithm: ai_query.Algorithm = ai_query.Algorithm__CosineSimilarity,
        condition: typing.Optional[ai_query.PredicateCondition] = None,
        preprocess_action: ai_query.PreprocessAction = ai_query.PreprocessAction__ModelPreprocessing,
        execution_provider: typing.Optional[ai_query.ExecutionProvider] = None,
        tracing_id: typing.Optional[str] = None,
    ):
        builder = AsyncAhnlichAIRequestBuilder(tracing_id)
        builder.get_sim_n(
            store_name=store_name,
            search_input=search_input,
            closest_n=closest_n,
            algorithm=algorithm,
            condition=condition,
            preprocess_action=preprocess_action,
            execution_provider=execution_provider,
        )
        return await self.process_request(builder.to_server_query())

    async def create_pred_index(
        self,
        store_name: str,
        predicates: typing.Sequence[str],
        tracing_id: typing.Optional[str] = None,
    ):
        builder = AsyncAhnlichAIRequestBuilder(tracing_id)
        builder.create_pred_index(store_name=store_name, predicates=predicates)
        return await self.process_request(builder.to_server_query())

    async def create_non_linear_algorithm_index(
        self,
        store_name: str,
        non_linear_indices: typing.Sequence["NonLinearAlgorithm"],
        tracing_id: typing.Optional[str] = None,
    ):
        builder = AsyncAhnlichAIRequestBuilder(tracing_id)
        builder.create_non_linear_algorithm_index(
            store_name=store_name, non_linear_indices=non_linear_indices
        )
        return await self.process_request(builder.to_server_query())

    async def drop_pred_index(
        self,
        store_name: str,
        predicates: typing.Sequence[str],
        error_if_not_exists: bool,
        tracing_id: typing.Optional[str] = None,
    ):
        builder = AsyncAhnlichAIRequestBuilder(tracing_id)
        builder.drop_pred_index(
            store_name=store_name,
            predicates=predicates,
            error_if_not_exists=error_if_not_exists,
        )
        return await self.process_request(builder.to_server_query())

    async def drop_non_linear_algorithm_index(
        self,
        store_name: str,
        non_linear_indices: typing.Sequence["NonLinearAlgorithm"],
        error_if_not_exists: bool,
        tracing_id: typing.Optional[str] = None,
    ):
        builder = AsyncAhnlichAIRequestBuilder(tracing_id)
        builder.drop_non_linear_algorithm_index(
            store_name=store_name,
            non_linear_indices=non_linear_indices,
            error_if_not_exists=error_if_not_exists,
        )
        return await self.process_request(builder.to_server_query())

    async def set(
        self,
        store_name: str,
        inputs: typing.Sequence[
            typing.Tuple[ai_query.StoreInput, typing.Dict[str, ai_query.MetadataValue]]
        ],
        preprocess_action: ai_query.PreprocessAction = ai_query.PreprocessAction__NoPreprocessing,
        execution_provider: typing.Optional[ai_query.ExecutionProvider] = None,
        tracing_id: typing.Optional[str] = None,
    ):
        builder = AsyncAhnlichAIRequestBuilder(tracing_id)
        builder.set(
            store_name=store_name,
            inputs=inputs,
            preprocess_action=preprocess_action,
            execution_provider=execution_provider,
        )
        return await self.process_request(builder.to_server_query())

    async def del_key(
        self,
        store_name: str,
        key: ai_query.StoreInput,
        tracing_id: typing.Optional[str] = None,
    ):
        builder = AsyncAhnlichAIRequestBuilder(tracing_id)
        builder.del_key(store_name=store_name, key=key)
        return await self.process_request(builder.to_server_query())

    async def get_key(
        self,
        store_name: str,
        keys: typing.Sequence[ai_query.StoreInput],
        tracing_id: typing.Optional[str] = None,
    ):
        builder = AsyncAhnlichAIRequestBuilder(tracing_id)
        builder.get_key(store_name=store_name, keys=keys)
        return await self.process_request(builder.to_server_query())

    async def drop_store(
        self,
        store_name: str,
        error_if_not_exists: bool = True,
        tracing_id: typing.Optional[str] = None,
    ):
        builder = AsyncAhnlichAIRequestBuilder(tracing_id)
        builder.drop_store(
            store_name=store_name, error_if_not_exists=error_if_not_exists
        )
        return await self.process_request(builder.to_server_query())

    async def purge_stores(
        self,
        tracing_id: typing.Optional[str] = None,
    ):
        builder = AsyncAhnlichAIRequestBuilder(tracing_id)
        builder.purge_stores()
        return await self.process_request(builder.to_server_query())

    async def info_server(
        self,
        tracing_id: typing.Optional[str] = None,
    ):
        builder = AsyncAhnlichAIRequestBuilder(tracing_id)
        builder.info_server()
        return await self.process_request(builder.to_server_query())

    async def list_stores(
        self,
        tracing_id: typing.Optional[str] = None,
    ):
        builder = AsyncAhnlichAIRequestBuilder(tracing_id)
        builder.list_stores()
        return await self.process_request(builder.to_server_query())

    async def list_clients(
        self,
        tracing_id: typing.Optional[str] = None,
    ):
        builder = AsyncAhnlichAIRequestBuilder(tracing_id)
        builder.list_clients()
        return await self.process_request(builder.to_server_query())

    async def ping(
        self,
        tracing_id: typing.Optional[str] = None,
    ):
        builder = AsyncAhnlichAIRequestBuilder(tracing_id)
        builder.ping()
        return await self.process_request(builder.to_server_query())

    def pipeline(
        self,
        tracing_id: typing.Optional[str] = None,
    ) -> AsyncAhnlichAIRequestBuilder:
        """Gives you a request builder to create multple requests"""
        return AsyncAhnlichAIRequestBuilder(tracing_id, client=self)
