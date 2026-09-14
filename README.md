# ZCARD

## An Open Game Media Format for Physical and Modern Game Distribution

**ZCARD** is an open game media format designed to bring the concept of the physical game cartridge into the modern era.

It is designed to combine:

* Physical game media
* Modern storage capacities
* Executable game data
* Game assets
* Updates
* Save data
* Configuration
* Downloadable content
* Persistent user data
* Game metadata
* Hardware and software compatibility information

The goal is simple:

> **A game should be able to live on a physical card again — without being limited to the technology of a ROM cartridge.**

---

# Why ZCARD?

Modern games are increasingly distributed as downloads.

Physical media still exists, but traditional cartridges and optical discs impose significant limitations:

* Limited storage
* Expensive manufacturing
* Read-only designs
* Separate download requirements
* Limited update mechanisms
* Proprietary formats
* Dependence on platform-specific systems

ZCARD proposes another approach.

Instead of treating physical media as a read-only ROM, ZCARD treats it as a **persistent game storage medium**.

```text
Traditional Cartridge

┌──────────────────────┐
│       ROM GAME       │
│                      │
│      READ ONLY       │
└──────────────────────┘


ZCARD

┌──────────────────────────────┐
│           ZCARD              │
├──────────────────────────────┤
│ Game Metadata                │
│ Executable                   │
│ Game Assets                  │
│ Runtime Data                 │
│ Updates                      │
│ DLC                          │
│ Configuration                │
│ Save Data                    │
│ User Data                    │
└──────────────────────────────┘
```

---

# What is ZCARD?

ZCARD is a **game media and container specification**.

It defines how a game can be organized, stored, identified and accessed independently of the physical technology used to store it.

The same logical ZCARD can exist as:

```text
Physical ZCARD
      │
      ├── Flash storage
      ├── Future ZCARD hardware
      └── Other compatible storage
     
Digital ZCARD
      │
      ├── .zcard file
      ├── Development image
      └── Emulator image
```

The physical implementation is therefore separated from the logical format.

---

# Design Goals

ZCARD is designed around several principles.

## 1. Persistent physical media

A ZCARD should be capable of containing an entire game rather than acting only as a license or boot key.

## 2. Writable storage

The format is designed to allow writable areas for:

* Updates
* Saves
* Configuration
* User data
* Downloadable content

while keeping the original game data identifiable and protected by the format.

## 3. Large capacity

ZCARD is not restricted to traditional cartridge capacities.

The logical format can scale from small games to very large modern games.

Possible physical capacities include:

```text
16 MB
32 MB
64 MB
128 MB

8 GB
16 GB
32 GB
64 GB
128 GB

256 GB+
```

These are examples of possible physical implementations, not requirements of the format.

## 4. Hardware independence

ZCARD describes the logical media format.

The underlying storage technology can evolve without requiring the game format to change.

## 5. Open development

The format is intended to be documented well enough that independent developers can create:

* Games
* Tools
* Builders
* Readers
* Emulators
* Hardware
* Development kits

without depending on a single proprietary implementation.

---

# ZCARD Architecture

A logical ZCARD can be divided into several areas.

```text
┌─────────────────────────────────────────┐
│                 ZCARD                   │
├─────────────────────────────────────────┤
│ HEADER                                  │
├─────────────────────────────────────────┤
│ METADATA                                │
├─────────────────────────────────────────┤
│ GAME EXECUTABLE                         │
├─────────────────────────────────────────┤
│ GAME ASSETS                             │
├─────────────────────────────────────────┤
│ OPTIONAL CONTENT                        │
├─────────────────────────────────────────┤
│ UPDATE DATA                             │
├─────────────────────────────────────────┤
│ SAVE / USER DATA                        │
├─────────────────────────────────────────┤
│ CONFIGURATION                           │
├─────────────────────────────────────────┤
│ INDEX / MANIFEST                        │
└─────────────────────────────────────────┘
```

The exact physical layout is implementation-dependent while the logical organization is defined by the ZCARD specification.

---

# Read-Only and Writable Data

One of the fundamental concepts of ZCARD is the separation between original game data and writable data.

```text
                  ZCARD
                    │
          ┌─────────┴─────────┐
          │                   │
     GAME REGION          USER REGION
          │                   │
     ┌────┴────┐         ┌────┴────┐
     │          │         │         │
   CODE       ASSETS     SAVES    CONFIG
     │          │         │         │
   READ       READ      WRITE     WRITE
```

The exact implementation of write protection depends on the physical ZCARD hardware.

The logical format, however, can identify which data belongs to the original game and which data is user-generated.

---

# ZCARD Contents

A ZCARD may contain:

```text
Game
├── Executable
├── Assets
│   ├── Textures
│   ├── Models
│   ├── Audio
│   ├── Video
│   └── Data
│
├── Metadata
│
├── Runtime
│
├── Updates
│
├── DLC
│
├── Saves
│
└── Configuration
```

A game does not need to use every component.

Small games may contain only:

```text
Game
├── Metadata
├── Executable
└── Assets
```

A larger game may use the complete architecture.

---

# Metadata

ZCARD metadata allows software and hardware to identify the game before execution.

Example:

```json
{
    "format": "ZCARD",
    "version": 1,
    "game": "Example Game",
    "developer": "Example Studio",
    "version": "1.0.0",
    "architecture": "ZConsole",
    "entry": "game.zexe"
}
```

Metadata may eventually include:

* Game title
* Developer
* Publisher
* Version
* Region
* Language
* Architecture
* Required runtime
* Required storage
* Minimum hardware
* Supported controllers
* Save requirements
* Content information

---

# Executable Format

ZCARD does not necessarily require games to contain raw machine code directly.

The reference ZConsole ecosystem uses **ZEXE** as an executable format.

```text
ZCARD
 │
 └── game.zexe
       │
       ▼
   ZConsole Runtime
       │
       ▼
   Target Hardware
```

ZEXE is therefore related to the ZCARD ecosystem, but it is conceptually separate from the ZCARD container itself.

This allows the ZCARD format to remain focused on **game media**, while ZEXE defines one possible executable representation.

---

# Asset Storage

ZCARD is designed to support large collections of game assets.

Examples:

```text
assets/
├── textures/
├── models/
├── shaders/
├── audio/
├── video/
├── levels/
└── data/
```

Assets may be loaded on demand instead of requiring the entire game to be copied into RAM.

This enables the format to support games significantly larger than available system memory.

---

# Asset Streaming

The ZCARD architecture supports the concept of streaming assets directly from the game medium.

```text
ZCARD
 │
 │ asset request
 ▼
Asset Manager
 │
 ├── Cache
 ├── Prefetch
 ├── Priority
 ├── Dependencies
 └── Streaming
 │
 ▼
Game Runtime
```

This is particularly important for large games.

A game may request only the assets required for the current scene instead of loading the entire game.

---

# Updates

ZCARD is designed with updates in mind.

An update does not necessarily need to replace the entire game.

Conceptually:

```text
Original ZCARD
      │
      ├── Game v1.0
      │
      └── Update
             │
             ▼
          Game v1.1
```

Future versions of the specification may define:

* Differential updates
* Patch manifests
* Version chains
* Update verification
* Rollback
* Multiple update slots

---

# Save Data

Save data is conceptually separated from the original game content.

```text
GAME DATA
──────────────
Executable
Assets
Metadata
Original Content


USER DATA
──────────────
Save
Configuration
Profiles
Progress
User Content
```

This separation allows physical implementations to protect the original game while providing writable storage.

---

# Digital Representation

During development and testing, ZCARD can be represented as a file.

Example:

```text
game.zcard
```

The digital representation makes it possible to:

* Develop games without physical hardware
* Test ZCARD readers
* Validate the specification
* Build automated tests
* Distribute development builds
* Use emulators
* Create CI pipelines

The digital representation is a **development and interoperability mechanism**, not a requirement that ZCARD remain a software-only format.

---

# Physical ZCARD

The long-term goal is a physical implementation.

```text
        ┌────────────────────────┐
        │        ZCARD           │
        │                        │
        │      Game Media        │
        │                        │
        │   Persistent Storage   │
        │                        │
        └───────────┬────────────┘
                    │
                    │
             ZCARD Interface
                    │
                    ▼
             ┌──────────────┐
             │   ZConsole   │
             └──────────────┘
```

The physical interface is intentionally separated from the logical file/container specification.

This allows different generations of ZCARD hardware to evolve without redefining the entire game format.

---

# Interface Concept

The physical ZCARD concept is intended to use a dedicated high-speed storage interface rather than exposing a conventional filesystem directly to the game.

The physical connector and electrical interface are currently experimental.

The project is investigating:

* High-speed differential communication
* Dedicated cartridge controllers
* Persistent flash storage
* Hardware identification
* Secure media identification
* Storage management
* Writable user regions

The physical interface is **not yet a finalized specification**.

---

# Why not simply use SD cards or USB?

ZCARD is intended to provide a platform-specific media abstraction rather than simply exposing generic storage.

A dedicated game medium can eventually provide:

* Deterministic identification
* Game-specific storage management
* Read/write region separation
* Hardware authentication
* Standardized metadata
* Game-oriented streaming
* Persistent game identity
* Console-level integration

The physical implementation can still use modern flash technology internally.

---

# Filesystem vs Container

ZCARD should not be confused with a conventional filesystem.

A filesystem answers:

> "How do I store files on this storage device?"

ZCARD answers:

> "How is a game represented as persistent media?"

The two concepts can coexist.

```text
Physical Storage
      │
      ▼
ZCARD Media Layer
      │
      ├── Game
      ├── Updates
      ├── Saves
      └── User Data
             │
             ▼
       Game Runtime
```

The goal is to allow the console to understand the game medium without exposing unnecessary storage implementation details to the game itself.

---

# Reference Implementation

The ZCARD project includes a reference implementation:

## ZCardEmulator

The **ZCardEmulator** is a development and testing tool for the ZCARD specification.

It is **not the ZCARD format itself**.

The emulator exists to provide a software environment in which developers can:

* Create ZCARD images
* Mount ZCARD images
* Inspect metadata
* Validate archives
* Test game packages
* Test ZEXE execution
* Test asset streaming
* Debug runtime behavior
* Experiment with future ZCARD features

```text
                 ZCARD SPECIFICATION
                         │
             ┌───────────┴───────────┐
             │                       │
       Physical ZCARD          Digital ZCARD
             │                       │
             │                 .zcard image
             │                       │
             └──────────┬────────────┘
                        │
                        ▼
                  ZCardEmulator
                        │
                        ▼
                  ZConsole Runtime
```

The emulator therefore acts as a **reference consumer of the format**.

---

# ZCARD Toolchain

The project is intended to eventually provide a complete toolchain:

```text
                 ZCARD
                   │
        ┌──────────┼──────────┐
        │          │          │
      Build      Validate    Test
        │          │          │
        ▼          ▼          ▼
   ZCARD Builder  Validator  Emulator
        │
        ▼
     game.zcard
        │
        ▼
 Physical ZCARD
```

Planned tools include:

* ZCARD Builder
* ZCARD Validator
* ZCARD Inspector
* ZCARD Emulator
* ZCARD SDK
* ZCARD Development Tools
* Physical ZCARD utilities

---

# Current Reference Implementation

The current reference implementation is written in **C++**.

Repository:

```text
ZCardEmulator
```

It currently provides experimental implementations of:

* ZCARD container handling
* ZCF container prototype
* ZEXE
* ZConsole runtime
* Virtual CPU
* Asset streaming
* Asset cache
* ZCARD Builder
* Archive validation
* Windows emulator dashboard
* Automated tests

The implementation exists primarily to validate the concepts described by the ZCARD project.

---

# Specification Status

| Component                       | Status                |
| ------------------------------- | --------------------- |
| ZCARD concept                   | Experimental          |
| Logical media architecture      | Experimental          |
| Digital `.zcard` representation | Implemented prototype |
| ZCARD Builder                   | Prototype             |
| ZCARD Validator                 | Prototype             |
| ZCF                             | Experimental          |
| ZEXE                            | Experimental          |
| ZConsole Runtime                | Experimental          |
| Emulator                        | Experimental          |
| Asset Streaming                 | Prototype             |
| Save Data Architecture          | Experimental          |
| Update Architecture             | Experimental          |
| Physical ZCARD                  | Research              |
| Electrical Interface            | Research              |
| Final Hardware Specification    | Not defined           |

---

# Versioning

ZCARD specifications use explicit versions.

Example:

```text
ZCARD Specification 0.1
```

Future incompatible changes should increment the major specification version.

A ZCARD should identify its format version in its header and/or metadata.

Example:

```text
format = ZCARD
version = 1
```

---

# Compatibility

A ZCARD implementation should identify:

* Format version
* Required runtime
* Architecture
* Optional capabilities
* Required features

This allows a console or emulator to determine whether it can execute a particular ZCARD.

Example:

```text
ZCARD
 │
 ├── Format: 1
 ├── Runtime: 1
 ├── Architecture: ZConsole
 └── Features:
       ├── Streaming
       ├── Save Data
       └── Updates
```

---

# Security

ZCARD implementations must treat game media as potentially untrusted input.

The reference implementation investigates protections including:

* Path traversal prevention
* Archive validation
* File size limits
* CRC validation
* Malformed archive detection
* Duplicate path detection
* Unsafe filenames
* Invalid metadata
* Malformed executable files
* Resource exhaustion

Future specifications may define:

* Digital signatures
* Developer certificates
* Game identity
* Secure updates
* Media authentication
* Anti-tampering mechanisms

Security features are still under development.

---

# Open Standard

The long-term objective is for ZCARD to be implementable by independent developers.

A healthy ZCARD ecosystem should allow different implementations to coexist:

```text
             ZCARD Specification
                     │
       ┌─────────────┼─────────────┐
       │             │             │
    Emulator       Console       Tools
       │             │             │
    Windows        Linux        Builder
                                 │
                              Hardware
```

No single implementation should define what ZCARD is.

The specification should.

---

# Roadmap

## Specification

* [x] Define initial ZCARD concept
* [x] Define logical media model
* [x] Define digital development representation
* [ ] Formal ZCARD header specification
* [ ] Formal metadata specification
* [ ] Formal region specification
* [ ] Formal manifest specification
* [ ] Compatibility specification
* [ ] Versioning specification
* [ ] Update specification
* [ ] Save-data specification
* [ ] Security specification

## Software

* [x] Reference emulator
* [x] ZCARD builder prototype
* [x] Archive validation
* [x] ZEXE prototype
* [x] ZConsole runtime prototype
* [x] Asset streaming prototype
* [ ] Standalone ZCARD validator
* [ ] ZCARD inspector
* [ ] Cross-platform reference tools
* [ ] Developer SDK

## Hardware

* [ ] Physical media prototype
* [ ] Storage controller
* [ ] Cartridge controller
* [ ] Physical connector prototype
* [ ] Communication protocol
* [ ] Hardware identification
* [ ] Writable region management
* [ ] Reference ZCARD board
* [ ] ZConsole prototype

---

# Documentation

The specification will be maintained separately from the reference emulator.

Planned documentation:

```text
docs/
├── ZCARD-SPECIFICATION.md
├── ZCARD-HEADER.md
├── ZCARD-MEDIA.md
├── ZCARD-MANIFEST.md
├── ZCARD-UPDATE.md
├── ZCARD-SAVE-DATA.md
├── ZCARD-SECURITY.md
├── ZCF.md
└── ZEXE.md
```

---

# Contributing

ZCARD is an experimental open project and contributions are welcome.

Areas of interest include:

* Format design
* Storage architecture
* Filesystems
* Game development
* Emulator development
* C++
* Embedded systems
* Flash storage
* Hardware design
* High-speed interfaces
* Graphics
* Runtime systems
* Security
* Documentation

For major changes to the format, please open a discussion before implementing the change.

Format compatibility is considered a priority.

---

# License

The ZCARD specification and reference implementation are currently under development.

See the repository license and individual component licenses for details.

---

# Project Status

**ZCARD is an experimental open game media format.**

The current software implementation is a reference implementation used to validate the architecture.

The physical cartridge is a future hardware objective.

The specification will evolve as the software and hardware prototypes provide new information.

---

# The Idea

Physical games should not have to disappear just because modern games became too large for traditional cartridges.

ZCARD explores another possibility:

```text
        1990s
          │
     GAME CARTRIDGE
          │
          ▼
     ┌───────────┐
     │   GAME    │
     └───────────┘

          ↓

        ZCARD
          │
     ┌────┴────┐
     │         │
   GAME      USER
   DATA      DATA
     │         │
     ├─ Code   ├─ Saves
     ├─ Assets ├─ Config
     ├─ DLC    └─ Updates
     └─ Data
          │
          ▼
      ZConsole
```

**ZCARD is an attempt to make physical game media relevant again — using modern storage instead of preserving the limitations of old cartridges.**

---

## ZCARD

**An open game media format for the next generation of physical games.**
