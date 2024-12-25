# Maintainer: Your Name <your.email@example.com>
pkgname=cli-sys-optimizer
pkgver=0.1.0
pkgrel=1
pkgdesc="A command-line system optimizer for Arch Linux."
arch=('any')
url="https://github.com/bishnoipk01/cli-sys-optimizer"
license=('MIT')
depends=('python')
makedepends=('python-setuptools' 'python-build' 'python-installer' 'python-wheel')
source=("$pkgname-$pkgver.tar.gz::https://github.com/bishnoipk01/cli-sys-optimizer/release/downlaod/0.1.0/cli_system_optimizer-$pkgver.tar.gz")
sha256sums=('SKIP')

build() {
    cd "$srcdir/$pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
