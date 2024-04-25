#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ROSE
Version  : 0.0.4
Release  : 11
URL      : https://cran.r-project.org/src/contrib/ROSE_0.0-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ROSE_0.0-4.tar.gz
Summary  : Random Over-Sampling Examples
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
problems in the presence of imbalanced classes. Synthetic balanced samples are  
  generated according to ROSE (Menardi and Torelli, 2013).  
  Functions that implement more traditional remedies to the class imbalance
  are also provided, as well as different metrics to evaluate a learner accuracy.
  These are estimated by holdout, bootstrap or cross-validation methods.

%prep
%setup -q -c -n ROSE
cd %{_builddir}/ROSE

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641103468

%install
export SOURCE_DATE_EPOCH=1641103468
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ROSE
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ROSE
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ROSE
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ROSE || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ROSE/CITATION
/usr/lib64/R/library/ROSE/ChangeLog
/usr/lib64/R/library/ROSE/DESCRIPTION
/usr/lib64/R/library/ROSE/INDEX
/usr/lib64/R/library/ROSE/Meta/Rd.rds
/usr/lib64/R/library/ROSE/Meta/data.rds
/usr/lib64/R/library/ROSE/Meta/features.rds
/usr/lib64/R/library/ROSE/Meta/hsearch.rds
/usr/lib64/R/library/ROSE/Meta/links.rds
/usr/lib64/R/library/ROSE/Meta/nsInfo.rds
/usr/lib64/R/library/ROSE/Meta/package.rds
/usr/lib64/R/library/ROSE/NAMESPACE
/usr/lib64/R/library/ROSE/R/ROSE
/usr/lib64/R/library/ROSE/R/ROSE.rdb
/usr/lib64/R/library/ROSE/R/ROSE.rdx
/usr/lib64/R/library/ROSE/data/hacide.rda
/usr/lib64/R/library/ROSE/help/AnIndex
/usr/lib64/R/library/ROSE/help/ROSE.rdb
/usr/lib64/R/library/ROSE/help/ROSE.rdx
/usr/lib64/R/library/ROSE/help/aliases.rds
/usr/lib64/R/library/ROSE/help/paths.rds
/usr/lib64/R/library/ROSE/html/00Index.html
/usr/lib64/R/library/ROSE/html/R.css
