Install the developer build of ITK, ITKMinimalPathExtraction ITKTubetk:

    python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ itk itk-minimalpathextraction itk-tubetk

Setup for editable installation. Changes to code in src are
immediatelly reflected in the installed version.  Also installs
all dependencies needed for development and testing:

    pip install -e .[dev]

Prior to making a commit, please verify your code is compliant:

    pre-commit run --all-files

HINT:
QT Designer was used to define the layout.  On Windows, to launch
designer, use this command:

    qt6-tools.exe designer pytubeview.ui
