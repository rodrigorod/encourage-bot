# Encourage Discord Bot

Encourage bot is a discord bot that allows users to randomly get Inspirational quotes messages and gives motivational encouragements whenever someone says that he's sad/depressed.

## Usage

### Commands

Every commands starts with '$'.

> **\$help**

List all commands available.

> **\$quote**

The bot will message a randomly chosen quote

Response :

```
Encourage Bot
BOT
— Today at 00:00
Begin at once to live, and count each separate day as a separate life.

- Seneca
```

> **\$new [encouragment]**

Add a new encouragement quote

Response :

```
Encourage Bot
BOT
— Today at 00:00
New encouraging message added.
```

> **\$list**

The bot will display all encouragement quotes added by users.

Response:

```
ObservedList(value=["You're handsome", "Continue, you're great !"])
```

> **\$del _index_**

Response :

*Before* :

```
ObservedList(value=["You're handsome", "Continue, you're great !"])
```

Example :

```
$del 1
```

*After :*

```
ObservedList(value=["You're handsome"])
```

## API

The data source is given by ZenQuotes.io

![ZenQuotes.io Logo](https://zenquotes.io/img/zen-quotes-icon-180.png)

## History

- v.0.0.1, 2021-25-11, initial version

## Credits

Lead Developer - Rodrigo Carraco Rodrigues (@rodrigorod)

## License

License
The MIT License (MIT)

Copyright (c) 2021 Rodrigo Carraco Rodrigues

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
