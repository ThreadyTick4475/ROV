# ROV code

## Important note

The code does not work yet.

## Required packages

- cmake
- gcc-arm-none-eabi
- libnewlib-arm-none-eabi
- build-essential

## Installation

###### All commands listed are for BASH

Install the required dependencies:

```bash
sudo apt install cmake gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential
```

Clone this repository to your computer:

```bash
git clone --recurse-submodules https://github.com/ThreadyTick4475/ROV
```

Change into the bot code directory:

```bash
cd ROV/bot
```

Prepare dependencies:

```bash
sudo cmake ../
```

## ROV code compilation and execution

While in the directory `ROV/bot`, compile the bot code:

```bash
sudo make
```

Hold the `Bootsel` button on your raspberry pi pico while plugging it into your pc.

Use a file manager to copy the file `ROV/bot/bot/main.uf2` to the drive created by the raspberry pi called `RPI-RPI2`

The bot code should now be uploaded to your raspberry pi pico.

## Surface code execution

While in the directory `ROV/control` run the command-line control interface:

```bash
python3 cli.py
```