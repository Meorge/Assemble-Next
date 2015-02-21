# Assemble-Next
A Riivolution XML memory patch builder

<h2>Requirements</h2>
To run Assemble Next from source, you will need the following programs installed:
<ul>
<li>Python 3.4</li>
<li>PyQt5</li>
<li>Qt 5.4</li>
</ul>

<h2>XML Schema</h2>
When creating patches for Assemble Next, it's important to use the correct format. First, these are the components you need:
<ul>
<li>Name of your hack</li>
<li>A description of your hack</li>
<li>The offsets for NTSC and PAL regions (note: JPN not supported yet)</li>
<li>The original value</li>
</ul>

The format to create the XML patch for An is as follows <a href=https://bpaste.net/show/b6ac0ca5cfb2>here</a>.<br>

<h2>Credits</h2>
<ul>
<li>Me (Meorge) for designing the UI and implementing some stuff, like getting the slider, hexbar and spinner to move together.</li><br>
<li>RoadrunnerWMC for doing all the hard stuff I don't know how to do, like implementing the XML recognition and getting FTH to convert hex to float properly.</li> <br>
<li>John10v10 and Kinnay for working on codes for the program, so it actually has a purpose :P</li><br>
<li><a href=http://stackoverflow.com/users/119527/jonathon-reinhart>Jonathon Reinhart</a> from <b>Stack Overflow</b> for making most of the code for FTH (you can find the code I found <a href=http://stackoverflow.com/questions/23624212/how-to-convert-a-float-into-hex>here</a>). Also thanks to Yhg1s (AKA Thomas Wouters) from the <i>#Python</i> IRC channel for helping with the FTH converting float-to-hex.</li><br>
</ul>

<h2>Note</h2>
I developed this program entierly on OS X, and although I don't remember integrating any OS X-specific stuff into the program, there may be some things that I don't know about. If you find any of these things (or the program just acts up in any way), tell us what happened and we'll look into it.


Happy hacking!<br>
-- The Reggie Next Team
