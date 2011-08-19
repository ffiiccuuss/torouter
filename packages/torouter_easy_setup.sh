#!/bin/bash

echo "We're adding Torouter packages to your Debian system"

cat << 'EOF' > /tmp/torouter-repo.key
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1.4.9 (GNU/Linux)

mQENBE5MF30BCACy2Ywqme78KCxY0qEXxm0vpBYe9X2kTdaJMS65tLfjbuHJ+WO4
OKCJ5AJc7NMvZGpVucn4JPTRN34oReXzYWrlm0yfmqnRHm9sEJhDqNbSV6RML+9E
oikxj6w6uboVEnrbLPzsWEcSze28dLcqVzDMm3aHO0erjBMlUEN4a7rrU0MDf+SH
4rz0kkEaBj8gzX+cJQEU5uIdlcINFtL34cNIZPAB3O2ZOjvrDbWJcI6wG/ZfefDk
2z98eSzhJfTWKsjnPmSsp7QTu+lj+mJN7BBoLILLJ+xq1XPJfigiuQucK3k2xMBv
eYEpK+11af6/bt5+yQec8dyH7+feYnpY2gW9ABEBAAG0H3RvcnJvdXRlciBhcmNo
aXZlIGtleSAoMjAxMS0wOCmJAT4EEwECACgFAk5MF30CGwMFCQDtTgAGCwkIBwMC
BhUIAgkKCwQWAgMBAh4BAheAAAoJEJGCGDUEfmokfYEH/RzFD2x5j1kJ+1+F2pTN
bTochEBvT4gsKCcuT+i7Q4FaorVCePoAyjcW3HBGBNf6G0a37KmtPoQBqXZ2wxVN
7SDFFG4nH27z+OdkrZkUmwnjr3O5QskMuiOfkvpD0aRKvmB/MznxjBW9brJr63Gx
IGkdvvZad2V4+jEwTWiOAodWbYGX9A5CgWUL+SHFhsLe3B3ZMrvgbReJqbOGRBTR
nGWYjLH5K0lNLPNb8spKOxT/h5gKib9p5680hQG672n9EJGixfmvrCQF/3cqy2SG
CmfX5Tt7+l/C6LfyaHWHsQsjqVtCmwPjfQ1sRa1S9UPXjrZb/54kDUHfpUByB/ab
kGU=
=ZXbM
-----END PGP PUBLIC KEY BLOCK-----
EOF

apt-key add /tmp/torouter-repo.key
apt-get update
apt-get install -t torrouter -y torouter-prep

echo "We're going to trash your system now; you have 30 seconds to bail out!"
sleep 30 && /usr/bin/torouter_config.sh
