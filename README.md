# ZCard
ZCARD — an open, persistent game media format designed for physical cartridges, digital distribution, updates, saves and modern game storage.

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
```
