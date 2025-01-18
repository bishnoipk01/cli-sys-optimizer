# # Maintainer: Your Name <your.email@example.com>
# pkgname=cli_sys_optimizer
# pkgver=1.0.0
# pkgrel=1
# pkgdesc="A command-line system optimizer for Arch Linux."
# arch=('any')
# url="https://github.com/bishnoipk01/cli-sys-optimizer"
# license=('MIT')
# depends=('python')
# makedepends=('python-setuptools' 'python-build' 'python-installer' 'python-wheel')
# source=("$pkgname-$pkgver.tar.gz::https://github.com/bishnoipk01/cli-sys-optimizer/releases/download/1.0.0/cli_sys_optimizer-$pkgver.tar.gz")
# sha256sums=('SKIP')

# build() {
#     cd "$srcdir/$pkgname-$pkgver"
#     python -m build --wheel --no-isolation
# }

# package() {
#     cd "$srcdir/$pkgname-$pkgver"
#     python -m installer --destdir="$pkgdir" dist/*.whl
# }

# Maintainer: Your Name <your.email@example.com>
pkgname=optimizer
pkgver=1.0.0
pkgrel=1
pkgdesc="A system resource optimization CLI tool."
arch=('any')
url="https://github.com/bishnoipk01/cli-sys-optimizer"
license=('MIT')
depends=('python' 'python-psutil' 'python-click')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')


# Update the source to match your new directory or tarball
source=("${pkgname}-${pkgver}.tar.gz::file://${PWD}/optimizer-1.0.0.tar.gz")

# Replace with actual checksum after generating it
sha256sums=('5f1bf1f5d581c219b1f8798726d037099db737a41815a21beb8796734faea667')

prepare() {
    # If you are using the tarball, you may need to extract it manually
    tar -xvzf "${srcdir}/${pkgname}-${pkgver}.tar.gz"
}

build() {
    cd "${srcdir}/optimizer-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/optimizer-${pkgver}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

# vim: ts=2 sw=2 et: