# likes

"Likes" is a tag-driven static website generator for creating list website of stuff you like.

![wil screenshot](./wil/screenshot.png)

Live example can be found: [granitosaurus.rocks/likes](http://granitosaurus.rocks/likes)


## Installing 

Click "Use This Template" button on github repository.

Then clone the repository and install dependencies

```shell script
$ git clone https://github.com/YOU/likes
$ cd likes
$ poetry install --no-root
$ poetry shell
```

Done! You can test it via:

```shell script
$ invoke livereload
go to http://localhost:8000
```

## Usage

For detailed usage see official [Pelican documentation][pelican-docs] but as quick overview:

1. Create your entries as markdown files in `content/` directory following this template: 
    ```markdown
    # e.g. this would be /content/snakes.md
    Title: Snakes
    Date: 2020-02-01
    Tags: pet,animal,nature
    Summary: Short summary of the subject
    Thumb: snake.jpg  # taken from /content/img directory

    long blog body that can include anything you want as long as it's markdown or html.
    ```  
      _You can use `invoke new <title> <tags> <summary>` command shortcut._
   
2. Preview it in your browser:
    ```shell
    $ invoke livereload
    ```  
    go to [http://localhost:8000](http://localhost:8000)

3. publish the site on github:

    ```
    invoke github
    ```

5. Enable github pages option in your repository under `repository->settings->options->github pages` (select `master` branch) and go to http://your_username.github.io/likes

see `me` branch for real live example.

[pelican-docs]: https://docs.getpelican.com/
