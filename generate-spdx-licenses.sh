#!/bin/bash
# uncomment to debug
# set -x

printf "Checking for the required programs used by this script.\n"
# ensure we have required programs installed, if not install them.
for pkg in curl jq sed tar; do
    if ! dnf list --installed "$pkg" &>/dev/null; then
        echo "Installing $pkg..."
        sudo dnf in "$pkg" -y
    else
        echo "$pkg is already installed."
    fi
done

printf "Downloading latest SPDX licence-list-data release from upstream..\n"

# Get latest release version tag
latest_version=$(curl -s https://api.github.com/repos/spdx/license-list-data/releases/latest | jq -r '.tag_name')
# strip any prepended v from version tag
version=${latest_version#v}
archive_url="https://github.com/spdx/license-list-data/archive/${latest_version}/${latest_version}.tar.gz"
# Download latest release as spdx-latest-release.tar.gz
curl -Ls ${archive_url} -o spdx-latest-release.tar.gz
# Extract licences.json from archive into pwd.
tar -xf spdx-latest-release.tar.gz --strip-components=2 license-list-data-${version}/json/licenses.json
tar -xf spdx-latest-release.tar.gz --strip-components=2 license-list-data-${version}/json/exceptions.json


printf "Generating licenses.toml file from downloaded JSON and discarding licenses marked deprecated.\n"
# Generate licenses.toml while filtering out deprecated licence entries.
LICENSE_ARRAY=$(jq -r '[.. | objects | select(.isDeprecatedLicenseId == false ) .licenseId? // empty] | map("\"" + . + "\"") | join(",\n\t")' licenses.json) && echo "ValidLicenses = [${LICENSE_ARRAY}]" \
	| sed 's/\[/[\n\t/' \
	| sed $'s/\]/,\\\n\]\\\n/g' > licenses.toml

printf "Generating exceptions array and appending to licenses.toml and discarding licenses marked deprecated.\n"
EXCEPTIONS_ARRAY=$(jq -r '[.. | objects | select(.isDeprecatedLicenseId == false ) .licenseExceptionId? // empty] | map("\"" + . + "\"") | join(",\n\t")' exceptions.json) && echo "ValidLicenseExceptions = [${EXCEPTIONS_ARRAY}]" \
	| sed 's/\[/[\n\t/' \
	| sed $'s/\]/,\\\n\]/g' \
	| tee -a licenses.toml >/dev/null

printf "Cleaning up downloaded files.\n"
rm -f spdx-latest-release.tar.gz licenses.json
printf "Operation completed.\n"
