slug: generating-a-gource-source-commit-history-visualization-for-qgis-quantum-gis
title: Generating a Gource source commit history visualization for QGIS (Quantum GIS)
categories:
- Open Source
- qgis
tags:
- git
- Gource
- mapping
- Open Source
- qgis
- Quantum GIS

A couple of days I found a pretty cool open source project for visualizing the history of version controlled code.  The project is called Gource and can be found here: [http://code.google.com/p/gource/](http://code.google.com/p/gource/) On the videos wiki page there are a few videos of other projects that have used gource to generate cool videos of their commit history so I thought I should make one for QGIS.

After downloading and building the latest source for Gource and fetching the current trunk of QGIS following these instructions: [http://spatialgalaxy.net/2010/12/27/contributing-to-qgis-using-git/](http://spatialgalaxy.net/2010/12/27/contributing-to-qgis-using-git/) I ran the following in my terminal on my Ubuntu machine, with my current directory being the download git repo from the above instructions:

    
      gource --title "Quantum GIS" --logo images\icons\qgis-icon.png \
      --hide filenames --date-format "%d, %B %Y" --seconds-per-day 0.15 \
      --highlight-all-users --auto-skip-seconds 0.5 --file-idle-time 0 --max-files 999999999 \
      --multi-sampling --stop-at-end --elasticity 0.1 -b 000000 \
      --disable-progress --user-friction .2 --output-ppm-stream - | \
      ffmpeg -an -threads 4 -y -b 3000K -vb 8000000 -r 60 -f image2pipe \
      -vcodec ppm -i - -vcodec libx264 -vpre libx264-medium qgis.mp4


Don't worry I know it looks crazy but it's really not that bad.  I'll break it down.



	
  * --title "Quantum GIS" **_Well, yeah, adds a title to the project._**

	
  * --logo images/icons/qgis-icon.png **_Adds a icon watermark_**

	
  * --hide filenames _**This hides the filenames of the files being committed .  I hide these because it makes it pretty hard to see.**_

	
  * --date-format "%d, %B %Y" **_Formats the date at the top of the video._**

	
  * --seconds-per-day 0.15 **_How many seconds represent a day.  The lower this is the fast a day goes by, meaning me commits in less time._**

	
  * --highlight-all-users **_Highlights all the users all the time._**

	
  * --auto-skip-seconds 0.5 **_If there are no commits for this time it will skip to the next commit._**

	
  * --file-idle-time 0 **_How long before the file disappears from the video, 0 means never good for seeing the full file tree._**

	
  * --stop-at-end **_Stops the video at the end of all the commits._**

	
  * -b 000000 **_The background colour, in this case black._**

	
  * --output-ppm-stream - **_Tells gource to output the result ppm stream to STDOUT, which is then piped ( | ) into the ffmpeg_**


That is a quick overview of some of the gource arguments, running grouce -H in your terminal will print out the full list.  I'm not going to go into the ffmpeg arguments because frankly I don't understand them very well and video isn't really my thing.  I'm sure there are ffmpeg experts that would be able to do it better then what I have.

After running the above commands in my terminal window and letting it do its thing, I had a resulting mp4 file which I then uploaded to YouTube.

Below is the video that I uploaded to YouTube, which took about 5 hours due to my very very slow (read 138kb/s) upload speed.  The video is about 8 years of QGIS development in just over 9 minutes.

As it's a bit hard to see in the video due to the quality, each cluster of files is a directory and the branches show the folder hierarchy.

[youtube=http://www.youtube.com/watch?v=-NILKRiMtcU]

Direct link to video: [http://www.youtube.com/watch?v=-NILKRiMtcU](http://www.youtube.com/watch?v=-NILKRiMtcU)

Happy new year and happy coding :)
