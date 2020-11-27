from subprocess import call

package = input("package: ")
call("cd C:\\Lorenzo\\Sviluppo\\Haskell\\libs", shell=True)
call("cabal install --lib --package-env . " + package, shell=True)