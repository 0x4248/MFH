# Multi File hash

Multi File Hash creates several hashes of the head and tail of a file.

## Usage

```bash
usage: mfh [-h] [-hl HL] [-tl TL] [-o O] [-cf CF] [-ch CH] file

Multi File Hash

positional arguments:
  file        File to hash

optional arguments:
  -h, --help  show this help message and exit
  -hl HL      Number of head lines to hash
  -tl TL      Number of tail lines to hash
  -o O        Output file
  -cf CF      Compare with other file (non hash file)
  -ch CH      Compare with other hash file
```

## Output

The output of the hash is in plain text and contains the following information:

```
MFH v1
fn:test.txt
ln:20
fs:355
sha256:cfa295bd6921065aea9750d7e779f63cf3f82d2b3be0b1d4ce25726f0371bbb0
HEAD:
h1:c7be1ed902fb8dd4d48997c6452f5d7e509fbcdbe2808b16bcf4edce4c07d14e
h2:d49482bf122a2d1d004f9043e4b4f16b071b0ac3ecdb5085e88c3cc09a222a53
h3:c7be1ed902fb8dd4d48997c6452f5d7e509fbcdbe2808b16bcf4edce4c07d14e
h4:178d71befa3a0798c0ae6c913ebf148da17fe73299d29d13170ef9111354dfad
h5:5432d71a67aac7a9be5afba29eff55a6483ee0b7805811b7fad2c5374b281a9e
h6:50413792adea477f01d4f34b47fa84896f84046eb083a6c1b65c854760c46d0a
h7:5432d71a67aac7a9be5afba29eff55a6483ee0b7805811b7fad2c5374b281a9e
h8:15d29fdeef396b994223ff63255c7699449e15c07d263d4615376cec9515b8a9
h9:10b6d204888f86f96806d86801aa1acc3271e820fe3ed78c6e1cfd24197ca946
h10:2a113222eddf98175694d093a02741502097af913ee4a4dcf8e8a54874699918
TAIL:
t11:c6969d5c58ad608183bff8fc0fd452af049aef230eff6b4697a27c4a24170974
t12:00f3ac0409eba1058b8d762f61c5342f01aefe4ae5b2d48f8bc0f9c494a282b2
t13:30651b703b9fbbf1d22f9ddeba41c21c479d3a0834e1516477d75eeadc52f391
t14:583ccb84539392b3a009b2df5f6d2e5147b3ea3bb6e275d6adb06de0836c1340
t15:86c6207321556f1480894cce769e5c76bc3fae5cc02c850cd8424a4989fa50f0
t16:fd0ec15b593224f9f692582afbb690e64fda4c2ae68b1aebd4769f001f973b72
t17:5dc975f5bfb8b00fcd8d9d815a8f78f334d53c83fa6152a1665467c2d7031681
t18:fd0ec15b593224f9f692582afbb690e64fda4c2ae68b1aebd4769f001f973b72
t19:5dc975f5bfb8b00fcd8d9d815a8f78f334d53c83fa6152a1665467c2d7031681
t20:fd0ec15b593224f9f692582afbb690e64fda4c2ae68b1aebd4769f001f973b72
```

- fn - File name
- ln - Number of lines
- fs - File size
- sha256 - SHA256 hash of the file
- HEAD - SHA256 hash of the head lines of the file
- TAIL - SHA256 hash of the tail lines of the file

## Licence

This project is licenced under the GNU General Public Licence v3.0 - see the [LICENCE](LICENCE) file for details
