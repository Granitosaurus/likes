# WIL

"What I Like" is a tag-driven static website generator for creating list website of stuff you like.

![wil screenshot](./wil/screenshot.png)

Live example can be found: [granitosaurus.rocks/wil](http://granitosaurus.rocks/wil)


## Installing 

Clone repository and install `pelican` for python:

```shell script
$ git clone https://github.com/Granitosaurus/wil -b source
$ pip install pelican[markdown]
$ cd wil
```

## Usage

For detailed usage see official [Pelican documentation][pelican-docs] but as quick overview:

1. Create your entries as markdown files in `content` directory following this template:  
    ```markdown
    # e.g. this would be /content/snakes.md
    Title: Snakes
    Date: 2020-02-01
    Tags: pet,animal,nature
    Summary: Short summary of the subject
    Thumb: snake.jpg  # taken from /content/thumb directory

    long blog body that can include anything you want as long as it's markdown or html.
    ```  
   
2. Preview it in your browser:
    ```shell
    $ make devserver
    ```  
    go to [http://localhost:8000](http://localhost:8000)

3. set your remote repository:

    ```shell script
    git remote remove origin
    git remote add origin <your repo> 
    ```

4. publish the changes:

    ```
    make github
    ```

5. Enable github pages option in your repository under `repository->settings->options->github pages` and go to http://your_username.github.io/wil

see `me` branch for real live example.

[pelican-docs]: https://docs.getpelican.com/
