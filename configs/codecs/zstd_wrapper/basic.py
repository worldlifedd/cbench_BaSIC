from configs.class_builder import ClassBuilder, ParamSlot
import cbench.codecs

config = ClassBuilder(
    cbench.codecs.ZstdWrapperCodec,
    # compressor_config=ParamSlot("level", 
    #     choices={i: dict(level=i) for i in range(1, 23)},
    #     default=dict(level=3),
    # )
)
