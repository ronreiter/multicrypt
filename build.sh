pyinstaller multicrypt.spec -y
MULTICRYPT_VERSION=`python -c "import multicrypt; print(multicrypt.__version__)"`

if [ "${OSTYPE//[0-9.]/}" == "darwin" ]
then
    # i have no idea why this is needed
    cp -f icons/multicrypt.icns dist/Multicrypt.app/Contents/Resources/
    rm -f dist/Multicrypt-osx-$MULTICRYPT_VERSION.dmg
	hdiutil create -srcfolder dist/Multicrypt.app dist/Multicrypt-osx-$MULTICRYPT_VERSION.dmg

fi