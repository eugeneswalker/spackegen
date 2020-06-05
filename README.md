#### Basic Usage

```
$> chmod +x spackegen

$> ./spackegen
Usage: ./spackegen <os> <arch> <compiler> [<tag>, <tag>, ...]
```

#### Ubuntu 18.04, ppc64le, GCC 7.3.0
```
$> ./spackegen ubuntu18.04 ppc64le gcc@7.3.0
```

#### OLCF Ascent, using 'ascent' tag
```
$> ./spackegen rhel7 ppc64le gcc@6.4.0 ascent
```

#### Ubuntu 18.04, ppc64le, GCC 7.3.0, using 'nocuda' tag
```
$> ./spackegen ubuntu18.04 ppc64le gcc@7.3.0 nocuda
```
