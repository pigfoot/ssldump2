set (core_sources
    engine.c
)

add_library(core STATIC ${core_sources})

target_link_libraries(core
)

add_executable(ssldump
    main.c
)

install(TARGETS ssldump DESTINATION sbin)
