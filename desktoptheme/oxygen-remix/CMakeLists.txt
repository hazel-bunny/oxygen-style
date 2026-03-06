configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/metadata.json.cmake"
    "${CMAKE_CURRENT_BINARY_DIR}/metadata.json"
    @ONLY
)

install(
    FILES "${CMAKE_CURRENT_BINARY_DIR}/metadata.json"
    DESTINATION ${PLASMA_DATA_INSTALL_DIR}/desktoptheme/oxygen-remix
)

FILE(GLOB widgets widgets/*.svg)
plasma_install_desktoptheme_svgs(oxygen-remix SUBPATH widgets FILES ${widgets})

FILE(GLOB dialogs dialogs/*.svg)
plasma_install_desktoptheme_svgs(oxygen-remix SUBPATH dialogs FILES ${dialogs})

FILE(GLOB opaque opaque/widgets/*.svg)
plasma_install_desktoptheme_svgs(oxygen-remix SUBPATH opaque/widgets FILES ${opaque})

FILE(GLOB opaque opaque/dialogs/*.svg)
plasma_install_desktoptheme_svgs(oxygen-remix SUBPATH opaque/dialogs FILES ${opaque})

FILE(GLOB solid_widgets solid/widgets/*.svg)
plasma_install_desktoptheme_svgs(oxygen-remix SUBPATH solid/widgets FILES ${solid_widgets})
