# Golang

- [Golang](#golang)
  - [Introduction](#introduction)
  - [Variabes et types de données](#variabes-et-types-de-données)
    - [Les types de données](#les-types-de-données)
      - [Integers](#integers)
        - [Unsigned Integers](#unsigned-integers)
        - [Signed Integers](#signed-integers)
        - [Machine Dependent Types](#machine-dependent-types)
      - [Floating Point Numbers](#floating-point-numbers)
        - [Floats](#floats)
        - [Complex (Imaginary Parts)](#complex-imaginary-parts)
      - [Strings](#strings)
      - [Boleans](#boleans)
  - [Expression d'affection - implicite vs explicite](#expression-daffection---implicite-vs-explicite)
    - [Printf - Affiché le type d'une variable](#printf---affiché-le-type-dune-variable)
    - [Opérateur d'affectation d'expression](#opérateur-daffectation-dexpression)
    - [Les types par défauts](#les-types-par-défauts)
  - [](#)

## Introduction
<!-- 
    TODO : texte d'introduction qui décrit le document
-->
Voici l'exemple de notre premier programme en Go. C'est un simple *Hello World* afin de tester l'installation.

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello World !!")
}
```

Pour voir le résultat de notre code, il faut le compiler et l'executé. Pour tester, nous aller créer un fichier *main.go* et y mettre notre code. Une fois fait, nous allons demander à go de compiler et d'executé notre code à la volée. Pour se faire, nous allons utiliser la commande `go run main.go`.

## Variabes et types de données

Pour commencer, il est important de noté que Go est un language statiquement typé. Se qui signifie qu'une fois qu'une variable est déclarée elle ne pourra jamais changer de type durant la durée d'execution du programme.

Pour créer une variable, nous devons utiliser le mot-clé `var` suivit d'un nom. Le nom de la variable ne peut être constitué que de chiffre, de lettre et d'underscore. La variable ne doit pas non plus commencer par un chiffre. En plus d'un nom, il faut aussi déclarer le type de la variable.

```go
var test string
```

Dans cette exemple, j'ai créé une variable `test` de type string. Cette variable ne contient rien pour le moment. Je peux à tout moment lui assigné une valeur avec l'operateur `=`:

```go
var test string
test = "Hello World !!"
fmt.Println(test)
```

```bash
> Hello World !!
```

Nous avons la possibilité d'affecter une valeur a une variable lors de sa création :

```go
var test string = "Hello World !!"
fmt.Println(test)
```

```bash
> Hello World !!
```

### Les types de données

Voici la liste des types de données que Go nous met à disposition :

```go
var number uint = 726332
var float float32 = 22.222
var str string = "Hello le Monde !"
var boleans bool = true

fmt.Println(number, float, str, boleans)
```

```bash
> 726332 22.222 Hello le Monde ! true
```

#### Integers

##### Unsigned Integers

- uint8 / byte (0 - 255)
- uint16 (0 - 65535)
- uint32 (0 - 4294967295)
- uint64 (0 - 18446744073709551615)

##### Signed Integers

- int8 (-128 - 127)
- int16 (-32768 - 32767)
- int32 / rune (-2147483648 - 2147483647)
- int64 (-9223372036854775808 - 9223372036854775807)

##### Machine Dependent Types

- uint (32 or 64 bits)
- int (same size as uint)
- uintptr (an unsigned integer to store the uninterpreted bits of a pointer value)

#### Floating Point Numbers

##### Floats

- float32 (IEEE-754 32-bit floating-point numbers)
- float64 (IEEE-754 64-bit floating-point numbers)

##### Complex (Imaginary Parts)

- complex64 (Complex numbers with float32 real and imaginary parts)
- complex128 (Complex numbers with float64 real and imaginary parts)

#### Strings

- "Hello World"

#### Boleans

- true
- false

## Expression d'affection - implicite vs explicite

Go ne nous oblige pas à définir un type lors de la déclaration d'une variable. C'est une bonne pratique, mais nous ne sommes pas forcer de l'appliquer. Si nous ne définission aucun type pour une variable, le compilateur va deviner qu'elle est le type à utiliser et cela peu créer des effets de board.

### Printf - Affiché le type d'une variable

Il est possible d'afficher le type d'une variable grâce à la fonction `Printf()` du module `fmt`. `Printf()` de formatter le retour de print grâce à des flags. Pour afficher le type d'une variable, nous devons utiliser le flag `%T`.

```go
var number = 2
fmt.Printf("%T", number)
```

```bash
> int
```

Nous voyons ici que le compilateur à choisi le type `int` pour notre variable.

```go
var number = 2.22
fmt.Printf("%T", number)
```

```bash
> float64
```

Ici, le type choisi est `float64`.

### Opérateur d'affectation d'expression

Sous ce nom barabar se cache un opérateur (`:=`) qui permet de ne pas mettre le mot clé `var` lors de la déclaration d'une variable.

```go
number := 2.22
fmt.Printf("%T", number)
```

```bash
> float64
```

`:=` fonctionne exactement de la même manière que lors nous utilisions le mot clé `var`. Sa seul raison d'être et de rendre le code plus rapide à produire et à lire.

### Les types par défauts

Si nous ne définission pas de valeur lors de la création d'une variable, le compilateur va en affecter une automatiquement en fonction du type de la variable. Voici la liste des valeurs par défaut en fonction des type:

```go
var number uint
var float float64
var str string
var boolean bool

fmt.Println(number, float, str, boolean)
```

```bash
0 0  false
```

## 