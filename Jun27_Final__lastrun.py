#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Sun Jul 16 09:40:03 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code_condition
import random

# 变量定义
n_values = [1, 2]
image_lists = [
    ["01.png", "02.png", "03.png", "04.png", "05.png", "06.png", "07.png", "08.png", "09.png"],
    ['01.png', '02.png', '03.png', '04.png', '05.png', '06.png', '07.png', '08.png', '09.png', '10.png', '11.png', '12.png', '13.png', '14.png', '15.png', '16.png', '17.png', '18.png']
]
fixation_lists = [
    ['up.png', 'down.png', 'left.png', 'right.png', 'center.png', 'lu.png', 'ru.png', 'ld.png', 'rd.png'],
    ['center.png']
]

# 生成所有条件的列表
conditions = []
for n in n_values:
    for image_list in image_lists:
        for fixation_list in fixation_lists:
            conditions.append((n, image_list, fixation_list))
shuffle(conditions)



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'N-BACK_primary'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    '年级': '',
    '班级': '',
    '性别': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'],expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/isaachigher/Documents/psychopy/N-back_package/Jun27_Final__lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0.0000, 0.0000, 0.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "InsFrame" ---
key_resp = keyboard.Keyboard()
ins_start = visual.ImageStim(
    win=win,
    name='ins_start', 
    image='ins700x350.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(700, 350),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "prepare" ---
key_resp_6 = keyboard.Keyboard()
ins_1back = visual.ImageStim(
    win=win,
    name='ins_1back', 
    image='ins_1-back_700x350.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(700, 350),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
ins_2back = visual.ImageStim(
    win=win,
    name='ins_2back', 
    image='ins_2-back_700x350.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(700, 350),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
pic_01png_2 = visual.ImageStim(
    win=win,
    name='pic_01png_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-100, 0), size=(70, 70),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
pic_02png_2 = visual.ImageStim(
    win=win,
    name='pic_02png_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(100, 0), size=(70, 70),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "Stim" ---
image_bac = visual.ImageStim(
    win=win,
    name='image_bac', 
    image='background_grey.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
n_value = visual.TextStim(win=win, name='n_value',
    text='',
    font=None,
    pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);
num = visual.TextStim(win=win, name='num',
    text='No.',
    font='Open Sans',
    pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
testnum = visual.TextStim(win=win, name='testnum',
    text='',
    font='Open Sans',
    pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
thisimage = visual.ImageStim(
    win=win,
    name='thisimage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(60, 60),
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
key_resp_2 = keyboard.Keyboard()
sound_true = sound.Sound('A', secs=0.1, stereo=True, hamming=True,
    name='sound_true')
sound_true.setVolume(2.0)
sound_false = sound.Sound('A', secs=0.2, stereo=True, hamming=False,
    name='sound_false')
sound_false.setVolume(1.0)

# --- Initialize components for Routine "feedback" ---
image_bac_2 = visual.ImageStim(
    win=win,
    name='image_bac_2', 
    image='background_grey.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
# Run 'Begin Experiment' code from feedback_code
msg = ''
msgcolor = ''
ntext = '' 
ncolor=''

msg_response = visual.TextStim(win=win, name='msg_response',
    text='',
    font='simsong',
    pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
fixation_img = visual.ImageStim(
    win=win,
    name='fixation_img', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "prepare" ---
key_resp_6 = keyboard.Keyboard()
ins_1back = visual.ImageStim(
    win=win,
    name='ins_1back', 
    image='ins_1-back_700x350.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(700, 350),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
ins_2back = visual.ImageStim(
    win=win,
    name='ins_2back', 
    image='ins_2-back_700x350.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(700, 350),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
pic_01png_2 = visual.ImageStim(
    win=win,
    name='pic_01png_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-100, 0), size=(70, 70),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
pic_02png_2 = visual.ImageStim(
    win=win,
    name='pic_02png_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(100, 0), size=(70, 70),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "Stim" ---
image_bac = visual.ImageStim(
    win=win,
    name='image_bac', 
    image='background_grey.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
n_value = visual.TextStim(win=win, name='n_value',
    text='',
    font=None,
    pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);
num = visual.TextStim(win=win, name='num',
    text='No.',
    font='Open Sans',
    pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
testnum = visual.TextStim(win=win, name='testnum',
    text='',
    font='Open Sans',
    pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
thisimage = visual.ImageStim(
    win=win,
    name='thisimage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(60, 60),
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
key_resp_2 = keyboard.Keyboard()
sound_true = sound.Sound('A', secs=0.1, stereo=True, hamming=True,
    name='sound_true')
sound_true.setVolume(2.0)
sound_false = sound.Sound('A', secs=0.2, stereo=True, hamming=False,
    name='sound_false')
sound_false.setVolume(1.0)

# --- Initialize components for Routine "feedback" ---
image_bac_2 = visual.ImageStim(
    win=win,
    name='image_bac_2', 
    image='background_grey.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
# Run 'Begin Experiment' code from feedback_code
msg = ''
msgcolor = ''
ntext = '' 
ncolor=''

msg_response = visual.TextStim(win=win, name='msg_response',
    text='',
    font='simsong',
    pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
fixation_img = visual.ImageStim(
    win=win,
    name='fixation_img', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "prepare" ---
key_resp_6 = keyboard.Keyboard()
ins_1back = visual.ImageStim(
    win=win,
    name='ins_1back', 
    image='ins_1-back_700x350.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(700, 350),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
ins_2back = visual.ImageStim(
    win=win,
    name='ins_2back', 
    image='ins_2-back_700x350.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(700, 350),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
pic_01png_2 = visual.ImageStim(
    win=win,
    name='pic_01png_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-100, 0), size=(70, 70),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
pic_02png_2 = visual.ImageStim(
    win=win,
    name='pic_02png_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(100, 0), size=(70, 70),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "Stim" ---
image_bac = visual.ImageStim(
    win=win,
    name='image_bac', 
    image='background_grey.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
n_value = visual.TextStim(win=win, name='n_value',
    text='',
    font=None,
    pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);
num = visual.TextStim(win=win, name='num',
    text='No.',
    font='Open Sans',
    pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
testnum = visual.TextStim(win=win, name='testnum',
    text='',
    font='Open Sans',
    pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
thisimage = visual.ImageStim(
    win=win,
    name='thisimage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(60, 60),
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
key_resp_2 = keyboard.Keyboard()
sound_true = sound.Sound('A', secs=0.1, stereo=True, hamming=True,
    name='sound_true')
sound_true.setVolume(2.0)
sound_false = sound.Sound('A', secs=0.2, stereo=True, hamming=False,
    name='sound_false')
sound_false.setVolume(1.0)

# --- Initialize components for Routine "feedback" ---
image_bac_2 = visual.ImageStim(
    win=win,
    name='image_bac_2', 
    image='background_grey.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
# Run 'Begin Experiment' code from feedback_code
msg = ''
msgcolor = ''
ntext = '' 
ncolor=''

msg_response = visual.TextStim(win=win, name='msg_response',
    text='',
    font='simsong',
    pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
fixation_img = visual.ImageStim(
    win=win,
    name='fixation_img', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "prepare" ---
key_resp_6 = keyboard.Keyboard()
ins_1back = visual.ImageStim(
    win=win,
    name='ins_1back', 
    image='ins_1-back_700x350.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(700, 350),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
ins_2back = visual.ImageStim(
    win=win,
    name='ins_2back', 
    image='ins_2-back_700x350.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(700, 350),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
pic_01png_2 = visual.ImageStim(
    win=win,
    name='pic_01png_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-100, 0), size=(70, 70),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
pic_02png_2 = visual.ImageStim(
    win=win,
    name='pic_02png_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(100, 0), size=(70, 70),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "Stim" ---
image_bac = visual.ImageStim(
    win=win,
    name='image_bac', 
    image='background_grey.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
n_value = visual.TextStim(win=win, name='n_value',
    text='',
    font=None,
    pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);
num = visual.TextStim(win=win, name='num',
    text='No.',
    font='Open Sans',
    pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
testnum = visual.TextStim(win=win, name='testnum',
    text='',
    font='Open Sans',
    pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
thisimage = visual.ImageStim(
    win=win,
    name='thisimage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(60, 60),
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
key_resp_2 = keyboard.Keyboard()
sound_true = sound.Sound('A', secs=0.1, stereo=True, hamming=True,
    name='sound_true')
sound_true.setVolume(2.0)
sound_false = sound.Sound('A', secs=0.2, stereo=True, hamming=False,
    name='sound_false')
sound_false.setVolume(1.0)

# --- Initialize components for Routine "feedback" ---
image_bac_2 = visual.ImageStim(
    win=win,
    name='image_bac_2', 
    image='background_grey.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
# Run 'Begin Experiment' code from feedback_code
msg = ''
msgcolor = ''
ntext = '' 
ncolor=''

msg_response = visual.TextStim(win=win, name='msg_response',
    text='',
    font='simsong',
    pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
fixation_img = visual.ImageStim(
    win=win,
    name='fixation_img', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "prepare" ---
key_resp_6 = keyboard.Keyboard()
ins_1back = visual.ImageStim(
    win=win,
    name='ins_1back', 
    image='ins_1-back_700x350.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(700, 350),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
ins_2back = visual.ImageStim(
    win=win,
    name='ins_2back', 
    image='ins_2-back_700x350.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(700, 350),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
pic_01png_2 = visual.ImageStim(
    win=win,
    name='pic_01png_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-100, 0), size=(70, 70),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
pic_02png_2 = visual.ImageStim(
    win=win,
    name='pic_02png_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(100, 0), size=(70, 70),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "Stim" ---
image_bac = visual.ImageStim(
    win=win,
    name='image_bac', 
    image='background_grey.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
n_value = visual.TextStim(win=win, name='n_value',
    text='',
    font=None,
    pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);
num = visual.TextStim(win=win, name='num',
    text='No.',
    font='Open Sans',
    pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
testnum = visual.TextStim(win=win, name='testnum',
    text='',
    font='Open Sans',
    pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
thisimage = visual.ImageStim(
    win=win,
    name='thisimage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(60, 60),
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
key_resp_2 = keyboard.Keyboard()
sound_true = sound.Sound('A', secs=0.1, stereo=True, hamming=True,
    name='sound_true')
sound_true.setVolume(2.0)
sound_false = sound.Sound('A', secs=0.2, stereo=True, hamming=False,
    name='sound_false')
sound_false.setVolume(1.0)

# --- Initialize components for Routine "feedback" ---
image_bac_2 = visual.ImageStim(
    win=win,
    name='image_bac_2', 
    image='background_grey.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
# Run 'Begin Experiment' code from feedback_code
msg = ''
msgcolor = ''
ntext = '' 
ncolor=''

msg_response = visual.TextStim(win=win, name='msg_response',
    text='',
    font='simsong',
    pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
fixation_img = visual.ImageStim(
    win=win,
    name='fixation_img', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "prepare" ---
key_resp_6 = keyboard.Keyboard()
ins_1back = visual.ImageStim(
    win=win,
    name='ins_1back', 
    image='ins_1-back_700x350.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(700, 350),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
ins_2back = visual.ImageStim(
    win=win,
    name='ins_2back', 
    image='ins_2-back_700x350.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(700, 350),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
pic_01png_2 = visual.ImageStim(
    win=win,
    name='pic_01png_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-100, 0), size=(70, 70),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
pic_02png_2 = visual.ImageStim(
    win=win,
    name='pic_02png_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(100, 0), size=(70, 70),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "Stim" ---
image_bac = visual.ImageStim(
    win=win,
    name='image_bac', 
    image='background_grey.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
n_value = visual.TextStim(win=win, name='n_value',
    text='',
    font=None,
    pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);
num = visual.TextStim(win=win, name='num',
    text='No.',
    font='Open Sans',
    pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
testnum = visual.TextStim(win=win, name='testnum',
    text='',
    font='Open Sans',
    pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
thisimage = visual.ImageStim(
    win=win,
    name='thisimage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(60, 60),
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
key_resp_2 = keyboard.Keyboard()
sound_true = sound.Sound('A', secs=0.1, stereo=True, hamming=True,
    name='sound_true')
sound_true.setVolume(2.0)
sound_false = sound.Sound('A', secs=0.2, stereo=True, hamming=False,
    name='sound_false')
sound_false.setVolume(1.0)

# --- Initialize components for Routine "feedback" ---
image_bac_2 = visual.ImageStim(
    win=win,
    name='image_bac_2', 
    image='background_grey.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
# Run 'Begin Experiment' code from feedback_code
msg = ''
msgcolor = ''
ntext = '' 
ncolor=''

msg_response = visual.TextStim(win=win, name='msg_response',
    text='',
    font='simsong',
    pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
fixation_img = visual.ImageStim(
    win=win,
    name='fixation_img', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "prepare" ---
key_resp_6 = keyboard.Keyboard()
ins_1back = visual.ImageStim(
    win=win,
    name='ins_1back', 
    image='ins_1-back_700x350.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(700, 350),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
ins_2back = visual.ImageStim(
    win=win,
    name='ins_2back', 
    image='ins_2-back_700x350.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(700, 350),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
pic_01png_2 = visual.ImageStim(
    win=win,
    name='pic_01png_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-100, 0), size=(70, 70),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
pic_02png_2 = visual.ImageStim(
    win=win,
    name='pic_02png_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(100, 0), size=(70, 70),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "Stim" ---
image_bac = visual.ImageStim(
    win=win,
    name='image_bac', 
    image='background_grey.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
n_value = visual.TextStim(win=win, name='n_value',
    text='',
    font=None,
    pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);
num = visual.TextStim(win=win, name='num',
    text='No.',
    font='Open Sans',
    pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
testnum = visual.TextStim(win=win, name='testnum',
    text='',
    font='Open Sans',
    pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
thisimage = visual.ImageStim(
    win=win,
    name='thisimage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(60, 60),
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
key_resp_2 = keyboard.Keyboard()
sound_true = sound.Sound('A', secs=0.1, stereo=True, hamming=True,
    name='sound_true')
sound_true.setVolume(2.0)
sound_false = sound.Sound('A', secs=0.2, stereo=True, hamming=False,
    name='sound_false')
sound_false.setVolume(1.0)

# --- Initialize components for Routine "feedback" ---
image_bac_2 = visual.ImageStim(
    win=win,
    name='image_bac_2', 
    image='background_grey.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
# Run 'Begin Experiment' code from feedback_code
msg = ''
msgcolor = ''
ntext = '' 
ncolor=''

msg_response = visual.TextStim(win=win, name='msg_response',
    text='',
    font='simsong',
    pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
fixation_img = visual.ImageStim(
    win=win,
    name='fixation_img', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "prepare" ---
key_resp_6 = keyboard.Keyboard()
ins_1back = visual.ImageStim(
    win=win,
    name='ins_1back', 
    image='ins_1-back_700x350.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(700, 350),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
ins_2back = visual.ImageStim(
    win=win,
    name='ins_2back', 
    image='ins_2-back_700x350.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(700, 350),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
pic_01png_2 = visual.ImageStim(
    win=win,
    name='pic_01png_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-100, 0), size=(70, 70),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
pic_02png_2 = visual.ImageStim(
    win=win,
    name='pic_02png_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(100, 0), size=(70, 70),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "Stim" ---
image_bac = visual.ImageStim(
    win=win,
    name='image_bac', 
    image='background_grey.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
n_value = visual.TextStim(win=win, name='n_value',
    text='',
    font=None,
    pos=(0, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);
num = visual.TextStim(win=win, name='num',
    text='No.',
    font='Open Sans',
    pos=(-45, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
testnum = visual.TextStim(win=win, name='testnum',
    text='',
    font='Open Sans',
    pos=(-20, 275), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
thisimage = visual.ImageStim(
    win=win,
    name='thisimage', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(60, 60),
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
key_resp_2 = keyboard.Keyboard()
sound_true = sound.Sound('A', secs=0.1, stereo=True, hamming=True,
    name='sound_true')
sound_true.setVolume(2.0)
sound_false = sound.Sound('A', secs=0.2, stereo=True, hamming=False,
    name='sound_false')
sound_false.setVolume(1.0)

# --- Initialize components for Routine "feedback" ---
image_bac_2 = visual.ImageStim(
    win=win,
    name='image_bac_2', 
    image='background_grey.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(500, 500),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
# Run 'Begin Experiment' code from feedback_code
msg = ''
msgcolor = ''
ntext = '' 
ncolor=''

msg_response = visual.TextStim(win=win, name='msg_response',
    text='',
    font='simsong',
    pos=(0, 275), height=30.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
fixation_img = visual.ImageStim(
    win=win,
    name='fixation_img', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(30, 30),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# --- Initialize components for Routine "thanks" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='感谢你参加我们的实验！\n现在你可以挑选一个自己的礼品了！',
    font='simsong',
    pos=(0, 0), height=35.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "InsFrame" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
InsFrameComponents = [key_resp, ins_start]
for thisComponent in InsFrameComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "InsFrame" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *ins_start* updates
    if ins_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ins_start.frameNStart = frameN  # exact frame index
        ins_start.tStart = t  # local t and not account for scr refresh
        ins_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_start, 'tStartRefresh')  # time at next scr refresh
        ins_start.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InsFrameComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "InsFrame" ---
for thisComponent in InsFrameComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "InsFrame" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "prepare" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from anslist_code
# set environment
numcount = 1
piccenpos_cr = [166, 0, -166]
piccenpos_ar = [166, 0, -166]

# select condition
condition = conditions.pop()
n, image_list, fixation_list = condition

# add condition details to data document
condi = {
    'n=': n,
    'len=': len(image_list),
    'fix=': len(fixation_list)
}
thisExp.addData('condition', condi)
print('N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list),len(conditions))

# analyze the image list
pre_img = []
rom_imgs = image_list.copy()
for _ in range(n):
    temp = random.choice(rom_imgs)
    pre_img.append(temp)
    rom_imgs.remove(temp)

# 生成匹配刺激列表 match_list
match_list = []
ram = range(9 * n)
for _ in ram:
    match_image = random.choice(image_list)
    match_list.append([match_image, match_image])
for item in match_list:
    temp = image_list.copy()
    n1 = n
    while n1 > 1:
        temp.remove(item[n - n1])
        item.insert(n - n1 + 1, random.choice(temp))
        n1 -= 1

# 生成刺激列表 stim_list
stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
while remaining > 0:
    new_image = random.choice(image_list)
    index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
    if index < n:
        stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
        remaining -= 1
    elif index < len(stim_list_pre):
        prev_image = stim_list_pre[index - n][0]
        next_image = stim_list_pre[index][0]

        if new_image != prev_image and new_image != next_image:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
    else:
        if new_image != stim_list_pre[index - n][0]:
            stim_list_pre.insert(index, [new_image])
            remaining -= 1

stim_list = []
# 迭代遍历原始刺激列表拆包
for stim in stim_list_pre:
    if len(stim) > 1:  # 成对的元素
        for s in stim:
            stim_list.append(s)
    else:  # 单个元素
        stim_list.append(stim[0])

# 计算转换后列表中的元素数量
num_elements = len(stim_list)

# 复制 stim_list 生成 answer_list
answer_list = []

if n == 1:
    preimg_list=['01.png']
else:
    preimg_list=['01.png','02.png']
    
allimg_list = preimg_list + stim_list
#anscount = 0
for i in range(n, len(allimg_list)):
    if allimg_list[i] == allimg_list[i - n]:
        answer_list.append('f')
        #anscount += 1
    else:
        answer_list.append('j')
        
if n == 1:
    ncolor = 'yellow'
    ntext = '-1-'
else :
    ncolor = 'purple'
    ntext = '-2-'
    
#print("before experiment stim_list:", stim_list)
#print("before experiment answer_list:",answer_list)
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
pic_01png_2.setImage('01.png')
pic_02png_2.setImage('02.png')
# keep track of which components have finished
prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
for thisComponent in prepareComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "prepare" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_6.started')
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *ins_1back* updates
    if ins_1back.status == NOT_STARTED and n ==1:
        # keep track of start time/frame for later
        ins_1back.frameNStart = frameN  # exact frame index
        ins_1back.tStart = t  # local t and not account for scr refresh
        ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ins_1back.started')
        ins_1back.setAutoDraw(True)
    
    # *ins_2back* updates
    if ins_2back.status == NOT_STARTED and n ==2:
        # keep track of start time/frame for later
        ins_2back.frameNStart = frameN  # exact frame index
        ins_2back.tStart = t  # local t and not account for scr refresh
        ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ins_2back.started')
        ins_2back.setAutoDraw(True)
    
    # *pic_01png_2* updates
    if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        pic_01png_2.frameNStart = frameN  # exact frame index
        pic_01png_2.tStart = t  # local t and not account for scr refresh
        pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pic_01png_2.started')
        pic_01png_2.setAutoDraw(True)
    
    # *pic_02png_2* updates
    if pic_02png_2.status == NOT_STARTED and n == 2:
        # keep track of start time/frame for later
        pic_02png_2.frameNStart = frameN  # exact frame index
        pic_02png_2.tStart = t  # local t and not account for scr refresh
        pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pic_02png_2.started')
        pic_02png_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "prepare" ---
for thisComponent in prepareComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "prepare" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
condition1 = data.TrialHandler(nReps=20.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='condition1')
thisExp.addLoop(condition1)  # add the loop to the experiment
thisCondition1 = condition1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCondition1.rgb)
if thisCondition1 != None:
    for paramName in thisCondition1:
        exec('{} = thisCondition1[paramName]'.format(paramName))

for thisCondition1 in condition1:
    currentLoop = condition1
    # abbreviate parameter names if possible (e.g. rgb = thisCondition1.rgb)
    if thisCondition1 != None:
        for paramName in thisCondition1:
            exec('{} = thisCondition1[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Stim" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_exe
    this_number = numcount
    this_image = stim_list[numcount-1]
    response = ''
    #the central position of picture
    shuffle(piccenpos_cr)
    shuffle(piccenpos_ar)
    piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
    
    ans = answer_list[numcount-1]
    thisExp.addData('ans', ans)
    print("begin routine ","count",numcount,"img",this_image,"ans",ans)
    
    if key_resp_2.corr:
        response = True
    
    else : 
        response = False
    
    
    n_value.setColor(ncolor, colorSpace='rgb')
    n_value.setText(ntext)
    testnum.setText(this_number)
    thisimage.setPos(piccenpos)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    sound_true.setSound('A', secs=0.1, hamming=True)
    sound_true.setVolume(2.0, log=False)
    sound_false.setSound('B', secs=0.2, hamming=False)
    sound_false.setVolume(4.0, log=False)
    # keep track of which components have finished
    StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
    for thisComponent in StimComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Stim" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_bac* updates
        if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_bac.frameNStart = frameN  # exact frame index
            image_bac.tStart = t  # local t and not account for scr refresh
            image_bac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_bac.started')
            image_bac.setAutoDraw(True)
        
        # *n_value* updates
        if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            n_value.frameNStart = frameN  # exact frame index
            n_value.tStart = t  # local t and not account for scr refresh
            n_value.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
            n_value.setAutoDraw(True)
        
        # *num* updates
        if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            num.frameNStart = frameN  # exact frame index
            num.tStart = t  # local t and not account for scr refresh
            num.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
            num.setAutoDraw(True)
        
        # *testnum* updates
        if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            testnum.frameNStart = frameN  # exact frame index
            testnum.tStart = t  # local t and not account for scr refresh
            testnum.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
            testnum.setAutoDraw(True)
        
        # *thisimage* updates
        if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            thisimage.frameNStart = frameN  # exact frame index
            thisimage.tStart = t  # local t and not account for scr refresh
            thisimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
            thisimage.setAutoDraw(True)
        if thisimage.status == STARTED:  # only update if drawing
            thisimage.setImage(this_image, log=False)
        
        # *key_resp_2* updates
        if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            key_resp_2.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = key_resp_2.getKeys(keyList=['f','j'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                key_resp_2.rt = _key_resp_2_allKeys[0].rt
                # was this correct?
                if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_true
        if sound_true.status == NOT_STARTED and response==True:
            # keep track of start time/frame for later
            sound_true.frameNStart = frameN  # exact frame index
            sound_true.tStart = t  # local t and not account for scr refresh
            sound_true.tStartRefresh = tThisFlipGlobal  # on global time
            sound_true.play(when=win)  # sync with win flip
        if sound_true.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                sound_true.tStop = t  # not accounting for scr refresh
                sound_true.frameNStop = frameN  # exact frame index
                sound_true.stop()
        # start/stop sound_false
        if sound_false.status == NOT_STARTED and response==False:
            # keep track of start time/frame for later
            sound_false.frameNStart = frameN  # exact frame index
            sound_false.tStart = t  # local t and not account for scr refresh
            sound_false.tStartRefresh = tThisFlipGlobal  # on global time
            sound_false.play(when=win)  # sync with win flip
        if sound_false.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                sound_false.tStop = t  # not accounting for scr refresh
                sound_false.frameNStop = frameN  # exact frame index
                sound_false.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Stim" ---
    for thisComponent in StimComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_exe
    numcount += 1
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(ans).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for condition1 (TrialHandler)
    condition1.addData('key_resp_2.keys',key_resp_2.keys)
    condition1.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        condition1.addData('key_resp_2.rt', key_resp_2.rt)
    sound_true.stop()  # ensure sound has stopped at end of routine
    sound_false.stop()  # ensure sound has stopped at end of routine
    # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    shuffle(fixation_list)
    fiximg = fixation_list[0]
    
    
    #监听按键信息并给出反馈
    if key_resp_2.corr:
        response = True
        msg = '答对了!'
        msgcolor = 'green'
    
    else : 
        response = False
        msg = '答错了!'
        msgcolor = 'red'
    
    
    
    msg_response.setColor(msgcolor, colorSpace='rgb')
    msg_response.setText(msg)
    fixation_img.setImage(fiximg)
    # keep track of which components have finished
    feedbackComponents = [image_bac_2, msg_response, fixation_img]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_bac_2* updates
        if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_bac_2.frameNStart = frameN  # exact frame index
            image_bac_2.tStart = t  # local t and not account for scr refresh
            image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_bac_2.started')
            image_bac_2.setAutoDraw(True)
        if image_bac_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                image_bac_2.tStop = t  # not accounting for scr refresh
                image_bac_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                image_bac_2.setAutoDraw(False)
        
        # *msg_response* updates
        if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            msg_response.frameNStart = frameN  # exact frame index
            msg_response.tStart = t  # local t and not account for scr refresh
            msg_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'msg_response.started')
            msg_response.setAutoDraw(True)
        if msg_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                msg_response.tStop = t  # not accounting for scr refresh
                msg_response.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.stopped')
                msg_response.setAutoDraw(False)
        
        # *fixation_img* updates
        if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_img.frameNStart = frameN  # exact frame index
            fixation_img.tStart = t  # local t and not account for scr refresh
            fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_img.started')
            fixation_img.setAutoDraw(True)
        if fixation_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_img.tStop = t  # not accounting for scr refresh
                fixation_img.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                fixation_img.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 20.0 repeats of 'condition1'


# --- Prepare to start Routine "prepare" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from anslist_code
# set environment
numcount = 1
piccenpos_cr = [166, 0, -166]
piccenpos_ar = [166, 0, -166]

# select condition
condition = conditions.pop()
n, image_list, fixation_list = condition

# add condition details to data document
condi = {
    'n=': n,
    'len=': len(image_list),
    'fix=': len(fixation_list)
}
thisExp.addData('condition', condi)
print('N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list),len(conditions))

# analyze the image list
pre_img = []
rom_imgs = image_list.copy()
for _ in range(n):
    temp = random.choice(rom_imgs)
    pre_img.append(temp)
    rom_imgs.remove(temp)

# 生成匹配刺激列表 match_list
match_list = []
ram = range(9 * n)
for _ in ram:
    match_image = random.choice(image_list)
    match_list.append([match_image, match_image])
for item in match_list:
    temp = image_list.copy()
    n1 = n
    while n1 > 1:
        temp.remove(item[n - n1])
        item.insert(n - n1 + 1, random.choice(temp))
        n1 -= 1

# 生成刺激列表 stim_list
stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
while remaining > 0:
    new_image = random.choice(image_list)
    index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
    if index < n:
        stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
        remaining -= 1
    elif index < len(stim_list_pre):
        prev_image = stim_list_pre[index - n][0]
        next_image = stim_list_pre[index][0]

        if new_image != prev_image and new_image != next_image:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
    else:
        if new_image != stim_list_pre[index - n][0]:
            stim_list_pre.insert(index, [new_image])
            remaining -= 1

stim_list = []
# 迭代遍历原始刺激列表拆包
for stim in stim_list_pre:
    if len(stim) > 1:  # 成对的元素
        for s in stim:
            stim_list.append(s)
    else:  # 单个元素
        stim_list.append(stim[0])

# 计算转换后列表中的元素数量
num_elements = len(stim_list)

# 复制 stim_list 生成 answer_list
answer_list = []

if n == 1:
    preimg_list=['01.png']
else:
    preimg_list=['01.png','02.png']
    
allimg_list = preimg_list + stim_list
#anscount = 0
for i in range(n, len(allimg_list)):
    if allimg_list[i] == allimg_list[i - n]:
        answer_list.append('f')
        #anscount += 1
    else:
        answer_list.append('j')
        
if n == 1:
    ncolor = 'yellow'
    ntext = '-1-'
else :
    ncolor = 'purple'
    ntext = '-2-'
    
#print("before experiment stim_list:", stim_list)
#print("before experiment answer_list:",answer_list)
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
pic_01png_2.setImage('01.png')
pic_02png_2.setImage('02.png')
# keep track of which components have finished
prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
for thisComponent in prepareComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "prepare" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_6.started')
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *ins_1back* updates
    if ins_1back.status == NOT_STARTED and n ==1:
        # keep track of start time/frame for later
        ins_1back.frameNStart = frameN  # exact frame index
        ins_1back.tStart = t  # local t and not account for scr refresh
        ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ins_1back.started')
        ins_1back.setAutoDraw(True)
    
    # *ins_2back* updates
    if ins_2back.status == NOT_STARTED and n ==2:
        # keep track of start time/frame for later
        ins_2back.frameNStart = frameN  # exact frame index
        ins_2back.tStart = t  # local t and not account for scr refresh
        ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ins_2back.started')
        ins_2back.setAutoDraw(True)
    
    # *pic_01png_2* updates
    if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        pic_01png_2.frameNStart = frameN  # exact frame index
        pic_01png_2.tStart = t  # local t and not account for scr refresh
        pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pic_01png_2.started')
        pic_01png_2.setAutoDraw(True)
    
    # *pic_02png_2* updates
    if pic_02png_2.status == NOT_STARTED and n == 2:
        # keep track of start time/frame for later
        pic_02png_2.frameNStart = frameN  # exact frame index
        pic_02png_2.tStart = t  # local t and not account for scr refresh
        pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pic_02png_2.started')
        pic_02png_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "prepare" ---
for thisComponent in prepareComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "prepare" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
condition2 = data.TrialHandler(nReps=20.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='condition2')
thisExp.addLoop(condition2)  # add the loop to the experiment
thisCondition2 = condition2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCondition2.rgb)
if thisCondition2 != None:
    for paramName in thisCondition2:
        exec('{} = thisCondition2[paramName]'.format(paramName))

for thisCondition2 in condition2:
    currentLoop = condition2
    # abbreviate parameter names if possible (e.g. rgb = thisCondition2.rgb)
    if thisCondition2 != None:
        for paramName in thisCondition2:
            exec('{} = thisCondition2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Stim" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_exe
    this_number = numcount
    this_image = stim_list[numcount-1]
    response = ''
    #the central position of picture
    shuffle(piccenpos_cr)
    shuffle(piccenpos_ar)
    piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
    
    ans = answer_list[numcount-1]
    thisExp.addData('ans', ans)
    print("begin routine ","count",numcount,"img",this_image,"ans",ans)
    
    if key_resp_2.corr:
        response = True
    
    else : 
        response = False
    
    
    n_value.setColor(ncolor, colorSpace='rgb')
    n_value.setText(ntext)
    testnum.setText(this_number)
    thisimage.setPos(piccenpos)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    sound_true.setSound('A', secs=0.1, hamming=True)
    sound_true.setVolume(2.0, log=False)
    sound_false.setSound('B', secs=0.2, hamming=False)
    sound_false.setVolume(4.0, log=False)
    # keep track of which components have finished
    StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
    for thisComponent in StimComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Stim" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_bac* updates
        if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_bac.frameNStart = frameN  # exact frame index
            image_bac.tStart = t  # local t and not account for scr refresh
            image_bac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_bac.started')
            image_bac.setAutoDraw(True)
        
        # *n_value* updates
        if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            n_value.frameNStart = frameN  # exact frame index
            n_value.tStart = t  # local t and not account for scr refresh
            n_value.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
            n_value.setAutoDraw(True)
        
        # *num* updates
        if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            num.frameNStart = frameN  # exact frame index
            num.tStart = t  # local t and not account for scr refresh
            num.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
            num.setAutoDraw(True)
        
        # *testnum* updates
        if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            testnum.frameNStart = frameN  # exact frame index
            testnum.tStart = t  # local t and not account for scr refresh
            testnum.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
            testnum.setAutoDraw(True)
        
        # *thisimage* updates
        if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            thisimage.frameNStart = frameN  # exact frame index
            thisimage.tStart = t  # local t and not account for scr refresh
            thisimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
            thisimage.setAutoDraw(True)
        if thisimage.status == STARTED:  # only update if drawing
            thisimage.setImage(this_image, log=False)
        
        # *key_resp_2* updates
        if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            key_resp_2.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = key_resp_2.getKeys(keyList=['f','j'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                key_resp_2.rt = _key_resp_2_allKeys[0].rt
                # was this correct?
                if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_true
        if sound_true.status == NOT_STARTED and response==True:
            # keep track of start time/frame for later
            sound_true.frameNStart = frameN  # exact frame index
            sound_true.tStart = t  # local t and not account for scr refresh
            sound_true.tStartRefresh = tThisFlipGlobal  # on global time
            sound_true.play(when=win)  # sync with win flip
        if sound_true.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                sound_true.tStop = t  # not accounting for scr refresh
                sound_true.frameNStop = frameN  # exact frame index
                sound_true.stop()
        # start/stop sound_false
        if sound_false.status == NOT_STARTED and response==False:
            # keep track of start time/frame for later
            sound_false.frameNStart = frameN  # exact frame index
            sound_false.tStart = t  # local t and not account for scr refresh
            sound_false.tStartRefresh = tThisFlipGlobal  # on global time
            sound_false.play(when=win)  # sync with win flip
        if sound_false.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                sound_false.tStop = t  # not accounting for scr refresh
                sound_false.frameNStop = frameN  # exact frame index
                sound_false.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Stim" ---
    for thisComponent in StimComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_exe
    numcount += 1
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(ans).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for condition2 (TrialHandler)
    condition2.addData('key_resp_2.keys',key_resp_2.keys)
    condition2.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        condition2.addData('key_resp_2.rt', key_resp_2.rt)
    sound_true.stop()  # ensure sound has stopped at end of routine
    sound_false.stop()  # ensure sound has stopped at end of routine
    # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    shuffle(fixation_list)
    fiximg = fixation_list[0]
    
    
    #监听按键信息并给出反馈
    if key_resp_2.corr:
        response = True
        msg = '答对了!'
        msgcolor = 'green'
    
    else : 
        response = False
        msg = '答错了!'
        msgcolor = 'red'
    
    
    
    msg_response.setColor(msgcolor, colorSpace='rgb')
    msg_response.setText(msg)
    fixation_img.setImage(fiximg)
    # keep track of which components have finished
    feedbackComponents = [image_bac_2, msg_response, fixation_img]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_bac_2* updates
        if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_bac_2.frameNStart = frameN  # exact frame index
            image_bac_2.tStart = t  # local t and not account for scr refresh
            image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_bac_2.started')
            image_bac_2.setAutoDraw(True)
        if image_bac_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                image_bac_2.tStop = t  # not accounting for scr refresh
                image_bac_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                image_bac_2.setAutoDraw(False)
        
        # *msg_response* updates
        if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            msg_response.frameNStart = frameN  # exact frame index
            msg_response.tStart = t  # local t and not account for scr refresh
            msg_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'msg_response.started')
            msg_response.setAutoDraw(True)
        if msg_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                msg_response.tStop = t  # not accounting for scr refresh
                msg_response.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.stopped')
                msg_response.setAutoDraw(False)
        
        # *fixation_img* updates
        if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_img.frameNStart = frameN  # exact frame index
            fixation_img.tStart = t  # local t and not account for scr refresh
            fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_img.started')
            fixation_img.setAutoDraw(True)
        if fixation_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_img.tStop = t  # not accounting for scr refresh
                fixation_img.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                fixation_img.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 20.0 repeats of 'condition2'


# --- Prepare to start Routine "prepare" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from anslist_code
# set environment
numcount = 1
piccenpos_cr = [166, 0, -166]
piccenpos_ar = [166, 0, -166]

# select condition
condition = conditions.pop()
n, image_list, fixation_list = condition

# add condition details to data document
condi = {
    'n=': n,
    'len=': len(image_list),
    'fix=': len(fixation_list)
}
thisExp.addData('condition', condi)
print('N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list),len(conditions))

# analyze the image list
pre_img = []
rom_imgs = image_list.copy()
for _ in range(n):
    temp = random.choice(rom_imgs)
    pre_img.append(temp)
    rom_imgs.remove(temp)

# 生成匹配刺激列表 match_list
match_list = []
ram = range(9 * n)
for _ in ram:
    match_image = random.choice(image_list)
    match_list.append([match_image, match_image])
for item in match_list:
    temp = image_list.copy()
    n1 = n
    while n1 > 1:
        temp.remove(item[n - n1])
        item.insert(n - n1 + 1, random.choice(temp))
        n1 -= 1

# 生成刺激列表 stim_list
stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
while remaining > 0:
    new_image = random.choice(image_list)
    index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
    if index < n:
        stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
        remaining -= 1
    elif index < len(stim_list_pre):
        prev_image = stim_list_pre[index - n][0]
        next_image = stim_list_pre[index][0]

        if new_image != prev_image and new_image != next_image:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
    else:
        if new_image != stim_list_pre[index - n][0]:
            stim_list_pre.insert(index, [new_image])
            remaining -= 1

stim_list = []
# 迭代遍历原始刺激列表拆包
for stim in stim_list_pre:
    if len(stim) > 1:  # 成对的元素
        for s in stim:
            stim_list.append(s)
    else:  # 单个元素
        stim_list.append(stim[0])

# 计算转换后列表中的元素数量
num_elements = len(stim_list)

# 复制 stim_list 生成 answer_list
answer_list = []

if n == 1:
    preimg_list=['01.png']
else:
    preimg_list=['01.png','02.png']
    
allimg_list = preimg_list + stim_list
#anscount = 0
for i in range(n, len(allimg_list)):
    if allimg_list[i] == allimg_list[i - n]:
        answer_list.append('f')
        #anscount += 1
    else:
        answer_list.append('j')
        
if n == 1:
    ncolor = 'yellow'
    ntext = '-1-'
else :
    ncolor = 'purple'
    ntext = '-2-'
    
#print("before experiment stim_list:", stim_list)
#print("before experiment answer_list:",answer_list)
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
pic_01png_2.setImage('01.png')
pic_02png_2.setImage('02.png')
# keep track of which components have finished
prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
for thisComponent in prepareComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "prepare" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_6.started')
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *ins_1back* updates
    if ins_1back.status == NOT_STARTED and n ==1:
        # keep track of start time/frame for later
        ins_1back.frameNStart = frameN  # exact frame index
        ins_1back.tStart = t  # local t and not account for scr refresh
        ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ins_1back.started')
        ins_1back.setAutoDraw(True)
    
    # *ins_2back* updates
    if ins_2back.status == NOT_STARTED and n ==2:
        # keep track of start time/frame for later
        ins_2back.frameNStart = frameN  # exact frame index
        ins_2back.tStart = t  # local t and not account for scr refresh
        ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ins_2back.started')
        ins_2back.setAutoDraw(True)
    
    # *pic_01png_2* updates
    if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        pic_01png_2.frameNStart = frameN  # exact frame index
        pic_01png_2.tStart = t  # local t and not account for scr refresh
        pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pic_01png_2.started')
        pic_01png_2.setAutoDraw(True)
    
    # *pic_02png_2* updates
    if pic_02png_2.status == NOT_STARTED and n == 2:
        # keep track of start time/frame for later
        pic_02png_2.frameNStart = frameN  # exact frame index
        pic_02png_2.tStart = t  # local t and not account for scr refresh
        pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pic_02png_2.started')
        pic_02png_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "prepare" ---
for thisComponent in prepareComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "prepare" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
condition3 = data.TrialHandler(nReps=20.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='condition3')
thisExp.addLoop(condition3)  # add the loop to the experiment
thisCondition3 = condition3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCondition3.rgb)
if thisCondition3 != None:
    for paramName in thisCondition3:
        exec('{} = thisCondition3[paramName]'.format(paramName))

for thisCondition3 in condition3:
    currentLoop = condition3
    # abbreviate parameter names if possible (e.g. rgb = thisCondition3.rgb)
    if thisCondition3 != None:
        for paramName in thisCondition3:
            exec('{} = thisCondition3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Stim" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_exe
    this_number = numcount
    this_image = stim_list[numcount-1]
    response = ''
    #the central position of picture
    shuffle(piccenpos_cr)
    shuffle(piccenpos_ar)
    piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
    
    ans = answer_list[numcount-1]
    thisExp.addData('ans', ans)
    print("begin routine ","count",numcount,"img",this_image,"ans",ans)
    
    if key_resp_2.corr:
        response = True
    
    else : 
        response = False
    
    
    n_value.setColor(ncolor, colorSpace='rgb')
    n_value.setText(ntext)
    testnum.setText(this_number)
    thisimage.setPos(piccenpos)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    sound_true.setSound('A', secs=0.1, hamming=True)
    sound_true.setVolume(2.0, log=False)
    sound_false.setSound('B', secs=0.2, hamming=False)
    sound_false.setVolume(4.0, log=False)
    # keep track of which components have finished
    StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
    for thisComponent in StimComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Stim" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_bac* updates
        if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_bac.frameNStart = frameN  # exact frame index
            image_bac.tStart = t  # local t and not account for scr refresh
            image_bac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_bac.started')
            image_bac.setAutoDraw(True)
        
        # *n_value* updates
        if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            n_value.frameNStart = frameN  # exact frame index
            n_value.tStart = t  # local t and not account for scr refresh
            n_value.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
            n_value.setAutoDraw(True)
        
        # *num* updates
        if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            num.frameNStart = frameN  # exact frame index
            num.tStart = t  # local t and not account for scr refresh
            num.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
            num.setAutoDraw(True)
        
        # *testnum* updates
        if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            testnum.frameNStart = frameN  # exact frame index
            testnum.tStart = t  # local t and not account for scr refresh
            testnum.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
            testnum.setAutoDraw(True)
        
        # *thisimage* updates
        if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            thisimage.frameNStart = frameN  # exact frame index
            thisimage.tStart = t  # local t and not account for scr refresh
            thisimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
            thisimage.setAutoDraw(True)
        if thisimage.status == STARTED:  # only update if drawing
            thisimage.setImage(this_image, log=False)
        
        # *key_resp_2* updates
        if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            key_resp_2.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = key_resp_2.getKeys(keyList=['f','j'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                key_resp_2.rt = _key_resp_2_allKeys[0].rt
                # was this correct?
                if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_true
        if sound_true.status == NOT_STARTED and response==True:
            # keep track of start time/frame for later
            sound_true.frameNStart = frameN  # exact frame index
            sound_true.tStart = t  # local t and not account for scr refresh
            sound_true.tStartRefresh = tThisFlipGlobal  # on global time
            sound_true.play(when=win)  # sync with win flip
        if sound_true.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                sound_true.tStop = t  # not accounting for scr refresh
                sound_true.frameNStop = frameN  # exact frame index
                sound_true.stop()
        # start/stop sound_false
        if sound_false.status == NOT_STARTED and response==False:
            # keep track of start time/frame for later
            sound_false.frameNStart = frameN  # exact frame index
            sound_false.tStart = t  # local t and not account for scr refresh
            sound_false.tStartRefresh = tThisFlipGlobal  # on global time
            sound_false.play(when=win)  # sync with win flip
        if sound_false.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                sound_false.tStop = t  # not accounting for scr refresh
                sound_false.frameNStop = frameN  # exact frame index
                sound_false.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Stim" ---
    for thisComponent in StimComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_exe
    numcount += 1
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(ans).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for condition3 (TrialHandler)
    condition3.addData('key_resp_2.keys',key_resp_2.keys)
    condition3.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        condition3.addData('key_resp_2.rt', key_resp_2.rt)
    sound_true.stop()  # ensure sound has stopped at end of routine
    sound_false.stop()  # ensure sound has stopped at end of routine
    # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    shuffle(fixation_list)
    fiximg = fixation_list[0]
    
    
    #监听按键信息并给出反馈
    if key_resp_2.corr:
        response = True
        msg = '答对了!'
        msgcolor = 'green'
    
    else : 
        response = False
        msg = '答错了!'
        msgcolor = 'red'
    
    
    
    msg_response.setColor(msgcolor, colorSpace='rgb')
    msg_response.setText(msg)
    fixation_img.setImage(fiximg)
    # keep track of which components have finished
    feedbackComponents = [image_bac_2, msg_response, fixation_img]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_bac_2* updates
        if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_bac_2.frameNStart = frameN  # exact frame index
            image_bac_2.tStart = t  # local t and not account for scr refresh
            image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_bac_2.started')
            image_bac_2.setAutoDraw(True)
        if image_bac_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                image_bac_2.tStop = t  # not accounting for scr refresh
                image_bac_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                image_bac_2.setAutoDraw(False)
        
        # *msg_response* updates
        if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            msg_response.frameNStart = frameN  # exact frame index
            msg_response.tStart = t  # local t and not account for scr refresh
            msg_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'msg_response.started')
            msg_response.setAutoDraw(True)
        if msg_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                msg_response.tStop = t  # not accounting for scr refresh
                msg_response.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.stopped')
                msg_response.setAutoDraw(False)
        
        # *fixation_img* updates
        if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_img.frameNStart = frameN  # exact frame index
            fixation_img.tStart = t  # local t and not account for scr refresh
            fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_img.started')
            fixation_img.setAutoDraw(True)
        if fixation_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_img.tStop = t  # not accounting for scr refresh
                fixation_img.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                fixation_img.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 20.0 repeats of 'condition3'


# --- Prepare to start Routine "prepare" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from anslist_code
# set environment
numcount = 1
piccenpos_cr = [166, 0, -166]
piccenpos_ar = [166, 0, -166]

# select condition
condition = conditions.pop()
n, image_list, fixation_list = condition

# add condition details to data document
condi = {
    'n=': n,
    'len=': len(image_list),
    'fix=': len(fixation_list)
}
thisExp.addData('condition', condi)
print('N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list),len(conditions))

# analyze the image list
pre_img = []
rom_imgs = image_list.copy()
for _ in range(n):
    temp = random.choice(rom_imgs)
    pre_img.append(temp)
    rom_imgs.remove(temp)

# 生成匹配刺激列表 match_list
match_list = []
ram = range(9 * n)
for _ in ram:
    match_image = random.choice(image_list)
    match_list.append([match_image, match_image])
for item in match_list:
    temp = image_list.copy()
    n1 = n
    while n1 > 1:
        temp.remove(item[n - n1])
        item.insert(n - n1 + 1, random.choice(temp))
        n1 -= 1

# 生成刺激列表 stim_list
stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
while remaining > 0:
    new_image = random.choice(image_list)
    index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
    if index < n:
        stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
        remaining -= 1
    elif index < len(stim_list_pre):
        prev_image = stim_list_pre[index - n][0]
        next_image = stim_list_pre[index][0]

        if new_image != prev_image and new_image != next_image:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
    else:
        if new_image != stim_list_pre[index - n][0]:
            stim_list_pre.insert(index, [new_image])
            remaining -= 1

stim_list = []
# 迭代遍历原始刺激列表拆包
for stim in stim_list_pre:
    if len(stim) > 1:  # 成对的元素
        for s in stim:
            stim_list.append(s)
    else:  # 单个元素
        stim_list.append(stim[0])

# 计算转换后列表中的元素数量
num_elements = len(stim_list)

# 复制 stim_list 生成 answer_list
answer_list = []

if n == 1:
    preimg_list=['01.png']
else:
    preimg_list=['01.png','02.png']
    
allimg_list = preimg_list + stim_list
#anscount = 0
for i in range(n, len(allimg_list)):
    if allimg_list[i] == allimg_list[i - n]:
        answer_list.append('f')
        #anscount += 1
    else:
        answer_list.append('j')
        
if n == 1:
    ncolor = 'yellow'
    ntext = '-1-'
else :
    ncolor = 'purple'
    ntext = '-2-'
    
#print("before experiment stim_list:", stim_list)
#print("before experiment answer_list:",answer_list)
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
pic_01png_2.setImage('01.png')
pic_02png_2.setImage('02.png')
# keep track of which components have finished
prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
for thisComponent in prepareComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "prepare" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_6.started')
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *ins_1back* updates
    if ins_1back.status == NOT_STARTED and n ==1:
        # keep track of start time/frame for later
        ins_1back.frameNStart = frameN  # exact frame index
        ins_1back.tStart = t  # local t and not account for scr refresh
        ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ins_1back.started')
        ins_1back.setAutoDraw(True)
    
    # *ins_2back* updates
    if ins_2back.status == NOT_STARTED and n ==2:
        # keep track of start time/frame for later
        ins_2back.frameNStart = frameN  # exact frame index
        ins_2back.tStart = t  # local t and not account for scr refresh
        ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ins_2back.started')
        ins_2back.setAutoDraw(True)
    
    # *pic_01png_2* updates
    if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        pic_01png_2.frameNStart = frameN  # exact frame index
        pic_01png_2.tStart = t  # local t and not account for scr refresh
        pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pic_01png_2.started')
        pic_01png_2.setAutoDraw(True)
    
    # *pic_02png_2* updates
    if pic_02png_2.status == NOT_STARTED and n == 2:
        # keep track of start time/frame for later
        pic_02png_2.frameNStart = frameN  # exact frame index
        pic_02png_2.tStart = t  # local t and not account for scr refresh
        pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pic_02png_2.started')
        pic_02png_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "prepare" ---
for thisComponent in prepareComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "prepare" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
condition4 = data.TrialHandler(nReps=20.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='condition4')
thisExp.addLoop(condition4)  # add the loop to the experiment
thisCondition4 = condition4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCondition4.rgb)
if thisCondition4 != None:
    for paramName in thisCondition4:
        exec('{} = thisCondition4[paramName]'.format(paramName))

for thisCondition4 in condition4:
    currentLoop = condition4
    # abbreviate parameter names if possible (e.g. rgb = thisCondition4.rgb)
    if thisCondition4 != None:
        for paramName in thisCondition4:
            exec('{} = thisCondition4[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Stim" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_exe
    this_number = numcount
    this_image = stim_list[numcount-1]
    response = ''
    #the central position of picture
    shuffle(piccenpos_cr)
    shuffle(piccenpos_ar)
    piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
    
    ans = answer_list[numcount-1]
    thisExp.addData('ans', ans)
    print("begin routine ","count",numcount,"img",this_image,"ans",ans)
    
    if key_resp_2.corr:
        response = True
    
    else : 
        response = False
    
    
    n_value.setColor(ncolor, colorSpace='rgb')
    n_value.setText(ntext)
    testnum.setText(this_number)
    thisimage.setPos(piccenpos)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    sound_true.setSound('A', secs=0.1, hamming=True)
    sound_true.setVolume(2.0, log=False)
    sound_false.setSound('B', secs=0.2, hamming=False)
    sound_false.setVolume(4.0, log=False)
    # keep track of which components have finished
    StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
    for thisComponent in StimComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Stim" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_bac* updates
        if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_bac.frameNStart = frameN  # exact frame index
            image_bac.tStart = t  # local t and not account for scr refresh
            image_bac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_bac.started')
            image_bac.setAutoDraw(True)
        
        # *n_value* updates
        if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            n_value.frameNStart = frameN  # exact frame index
            n_value.tStart = t  # local t and not account for scr refresh
            n_value.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
            n_value.setAutoDraw(True)
        
        # *num* updates
        if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            num.frameNStart = frameN  # exact frame index
            num.tStart = t  # local t and not account for scr refresh
            num.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
            num.setAutoDraw(True)
        
        # *testnum* updates
        if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            testnum.frameNStart = frameN  # exact frame index
            testnum.tStart = t  # local t and not account for scr refresh
            testnum.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
            testnum.setAutoDraw(True)
        
        # *thisimage* updates
        if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            thisimage.frameNStart = frameN  # exact frame index
            thisimage.tStart = t  # local t and not account for scr refresh
            thisimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
            thisimage.setAutoDraw(True)
        if thisimage.status == STARTED:  # only update if drawing
            thisimage.setImage(this_image, log=False)
        
        # *key_resp_2* updates
        if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            key_resp_2.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = key_resp_2.getKeys(keyList=['f','j'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                key_resp_2.rt = _key_resp_2_allKeys[0].rt
                # was this correct?
                if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_true
        if sound_true.status == NOT_STARTED and response==True:
            # keep track of start time/frame for later
            sound_true.frameNStart = frameN  # exact frame index
            sound_true.tStart = t  # local t and not account for scr refresh
            sound_true.tStartRefresh = tThisFlipGlobal  # on global time
            sound_true.play(when=win)  # sync with win flip
        if sound_true.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                sound_true.tStop = t  # not accounting for scr refresh
                sound_true.frameNStop = frameN  # exact frame index
                sound_true.stop()
        # start/stop sound_false
        if sound_false.status == NOT_STARTED and response==False:
            # keep track of start time/frame for later
            sound_false.frameNStart = frameN  # exact frame index
            sound_false.tStart = t  # local t and not account for scr refresh
            sound_false.tStartRefresh = tThisFlipGlobal  # on global time
            sound_false.play(when=win)  # sync with win flip
        if sound_false.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                sound_false.tStop = t  # not accounting for scr refresh
                sound_false.frameNStop = frameN  # exact frame index
                sound_false.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Stim" ---
    for thisComponent in StimComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_exe
    numcount += 1
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(ans).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for condition4 (TrialHandler)
    condition4.addData('key_resp_2.keys',key_resp_2.keys)
    condition4.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        condition4.addData('key_resp_2.rt', key_resp_2.rt)
    sound_true.stop()  # ensure sound has stopped at end of routine
    sound_false.stop()  # ensure sound has stopped at end of routine
    # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    shuffle(fixation_list)
    fiximg = fixation_list[0]
    
    
    #监听按键信息并给出反馈
    if key_resp_2.corr:
        response = True
        msg = '答对了!'
        msgcolor = 'green'
    
    else : 
        response = False
        msg = '答错了!'
        msgcolor = 'red'
    
    
    
    msg_response.setColor(msgcolor, colorSpace='rgb')
    msg_response.setText(msg)
    fixation_img.setImage(fiximg)
    # keep track of which components have finished
    feedbackComponents = [image_bac_2, msg_response, fixation_img]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_bac_2* updates
        if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_bac_2.frameNStart = frameN  # exact frame index
            image_bac_2.tStart = t  # local t and not account for scr refresh
            image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_bac_2.started')
            image_bac_2.setAutoDraw(True)
        if image_bac_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                image_bac_2.tStop = t  # not accounting for scr refresh
                image_bac_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                image_bac_2.setAutoDraw(False)
        
        # *msg_response* updates
        if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            msg_response.frameNStart = frameN  # exact frame index
            msg_response.tStart = t  # local t and not account for scr refresh
            msg_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'msg_response.started')
            msg_response.setAutoDraw(True)
        if msg_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                msg_response.tStop = t  # not accounting for scr refresh
                msg_response.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.stopped')
                msg_response.setAutoDraw(False)
        
        # *fixation_img* updates
        if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_img.frameNStart = frameN  # exact frame index
            fixation_img.tStart = t  # local t and not account for scr refresh
            fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_img.started')
            fixation_img.setAutoDraw(True)
        if fixation_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_img.tStop = t  # not accounting for scr refresh
                fixation_img.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                fixation_img.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 20.0 repeats of 'condition4'


# --- Prepare to start Routine "prepare" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from anslist_code
# set environment
numcount = 1
piccenpos_cr = [166, 0, -166]
piccenpos_ar = [166, 0, -166]

# select condition
condition = conditions.pop()
n, image_list, fixation_list = condition

# add condition details to data document
condi = {
    'n=': n,
    'len=': len(image_list),
    'fix=': len(fixation_list)
}
thisExp.addData('condition', condi)
print('N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list),len(conditions))

# analyze the image list
pre_img = []
rom_imgs = image_list.copy()
for _ in range(n):
    temp = random.choice(rom_imgs)
    pre_img.append(temp)
    rom_imgs.remove(temp)

# 生成匹配刺激列表 match_list
match_list = []
ram = range(9 * n)
for _ in ram:
    match_image = random.choice(image_list)
    match_list.append([match_image, match_image])
for item in match_list:
    temp = image_list.copy()
    n1 = n
    while n1 > 1:
        temp.remove(item[n - n1])
        item.insert(n - n1 + 1, random.choice(temp))
        n1 -= 1

# 生成刺激列表 stim_list
stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
while remaining > 0:
    new_image = random.choice(image_list)
    index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
    if index < n:
        stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
        remaining -= 1
    elif index < len(stim_list_pre):
        prev_image = stim_list_pre[index - n][0]
        next_image = stim_list_pre[index][0]

        if new_image != prev_image and new_image != next_image:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
    else:
        if new_image != stim_list_pre[index - n][0]:
            stim_list_pre.insert(index, [new_image])
            remaining -= 1

stim_list = []
# 迭代遍历原始刺激列表拆包
for stim in stim_list_pre:
    if len(stim) > 1:  # 成对的元素
        for s in stim:
            stim_list.append(s)
    else:  # 单个元素
        stim_list.append(stim[0])

# 计算转换后列表中的元素数量
num_elements = len(stim_list)

# 复制 stim_list 生成 answer_list
answer_list = []

if n == 1:
    preimg_list=['01.png']
else:
    preimg_list=['01.png','02.png']
    
allimg_list = preimg_list + stim_list
#anscount = 0
for i in range(n, len(allimg_list)):
    if allimg_list[i] == allimg_list[i - n]:
        answer_list.append('f')
        #anscount += 1
    else:
        answer_list.append('j')
        
if n == 1:
    ncolor = 'yellow'
    ntext = '-1-'
else :
    ncolor = 'purple'
    ntext = '-2-'
    
#print("before experiment stim_list:", stim_list)
#print("before experiment answer_list:",answer_list)
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
pic_01png_2.setImage('01.png')
pic_02png_2.setImage('02.png')
# keep track of which components have finished
prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
for thisComponent in prepareComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "prepare" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_6.started')
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *ins_1back* updates
    if ins_1back.status == NOT_STARTED and n ==1:
        # keep track of start time/frame for later
        ins_1back.frameNStart = frameN  # exact frame index
        ins_1back.tStart = t  # local t and not account for scr refresh
        ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ins_1back.started')
        ins_1back.setAutoDraw(True)
    
    # *ins_2back* updates
    if ins_2back.status == NOT_STARTED and n ==2:
        # keep track of start time/frame for later
        ins_2back.frameNStart = frameN  # exact frame index
        ins_2back.tStart = t  # local t and not account for scr refresh
        ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ins_2back.started')
        ins_2back.setAutoDraw(True)
    
    # *pic_01png_2* updates
    if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        pic_01png_2.frameNStart = frameN  # exact frame index
        pic_01png_2.tStart = t  # local t and not account for scr refresh
        pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pic_01png_2.started')
        pic_01png_2.setAutoDraw(True)
    
    # *pic_02png_2* updates
    if pic_02png_2.status == NOT_STARTED and n == 2:
        # keep track of start time/frame for later
        pic_02png_2.frameNStart = frameN  # exact frame index
        pic_02png_2.tStart = t  # local t and not account for scr refresh
        pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pic_02png_2.started')
        pic_02png_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "prepare" ---
for thisComponent in prepareComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "prepare" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
condition5 = data.TrialHandler(nReps=20.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='condition5')
thisExp.addLoop(condition5)  # add the loop to the experiment
thisCondition5 = condition5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCondition5.rgb)
if thisCondition5 != None:
    for paramName in thisCondition5:
        exec('{} = thisCondition5[paramName]'.format(paramName))

for thisCondition5 in condition5:
    currentLoop = condition5
    # abbreviate parameter names if possible (e.g. rgb = thisCondition5.rgb)
    if thisCondition5 != None:
        for paramName in thisCondition5:
            exec('{} = thisCondition5[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Stim" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_exe
    this_number = numcount
    this_image = stim_list[numcount-1]
    response = ''
    #the central position of picture
    shuffle(piccenpos_cr)
    shuffle(piccenpos_ar)
    piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
    
    ans = answer_list[numcount-1]
    thisExp.addData('ans', ans)
    print("begin routine ","count",numcount,"img",this_image,"ans",ans)
    
    if key_resp_2.corr:
        response = True
    
    else : 
        response = False
    
    
    n_value.setColor(ncolor, colorSpace='rgb')
    n_value.setText(ntext)
    testnum.setText(this_number)
    thisimage.setPos(piccenpos)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    sound_true.setSound('A', secs=0.1, hamming=True)
    sound_true.setVolume(2.0, log=False)
    sound_false.setSound('B', secs=0.2, hamming=False)
    sound_false.setVolume(4.0, log=False)
    # keep track of which components have finished
    StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
    for thisComponent in StimComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Stim" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_bac* updates
        if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_bac.frameNStart = frameN  # exact frame index
            image_bac.tStart = t  # local t and not account for scr refresh
            image_bac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_bac.started')
            image_bac.setAutoDraw(True)
        
        # *n_value* updates
        if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            n_value.frameNStart = frameN  # exact frame index
            n_value.tStart = t  # local t and not account for scr refresh
            n_value.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
            n_value.setAutoDraw(True)
        
        # *num* updates
        if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            num.frameNStart = frameN  # exact frame index
            num.tStart = t  # local t and not account for scr refresh
            num.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
            num.setAutoDraw(True)
        
        # *testnum* updates
        if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            testnum.frameNStart = frameN  # exact frame index
            testnum.tStart = t  # local t and not account for scr refresh
            testnum.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
            testnum.setAutoDraw(True)
        
        # *thisimage* updates
        if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            thisimage.frameNStart = frameN  # exact frame index
            thisimage.tStart = t  # local t and not account for scr refresh
            thisimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
            thisimage.setAutoDraw(True)
        if thisimage.status == STARTED:  # only update if drawing
            thisimage.setImage(this_image, log=False)
        
        # *key_resp_2* updates
        if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            key_resp_2.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = key_resp_2.getKeys(keyList=['f','j'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                key_resp_2.rt = _key_resp_2_allKeys[0].rt
                # was this correct?
                if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_true
        if sound_true.status == NOT_STARTED and response==True:
            # keep track of start time/frame for later
            sound_true.frameNStart = frameN  # exact frame index
            sound_true.tStart = t  # local t and not account for scr refresh
            sound_true.tStartRefresh = tThisFlipGlobal  # on global time
            sound_true.play(when=win)  # sync with win flip
        if sound_true.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                sound_true.tStop = t  # not accounting for scr refresh
                sound_true.frameNStop = frameN  # exact frame index
                sound_true.stop()
        # start/stop sound_false
        if sound_false.status == NOT_STARTED and response==False:
            # keep track of start time/frame for later
            sound_false.frameNStart = frameN  # exact frame index
            sound_false.tStart = t  # local t and not account for scr refresh
            sound_false.tStartRefresh = tThisFlipGlobal  # on global time
            sound_false.play(when=win)  # sync with win flip
        if sound_false.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                sound_false.tStop = t  # not accounting for scr refresh
                sound_false.frameNStop = frameN  # exact frame index
                sound_false.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Stim" ---
    for thisComponent in StimComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_exe
    numcount += 1
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(ans).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for condition5 (TrialHandler)
    condition5.addData('key_resp_2.keys',key_resp_2.keys)
    condition5.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        condition5.addData('key_resp_2.rt', key_resp_2.rt)
    sound_true.stop()  # ensure sound has stopped at end of routine
    sound_false.stop()  # ensure sound has stopped at end of routine
    # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    shuffle(fixation_list)
    fiximg = fixation_list[0]
    
    
    #监听按键信息并给出反馈
    if key_resp_2.corr:
        response = True
        msg = '答对了!'
        msgcolor = 'green'
    
    else : 
        response = False
        msg = '答错了!'
        msgcolor = 'red'
    
    
    
    msg_response.setColor(msgcolor, colorSpace='rgb')
    msg_response.setText(msg)
    fixation_img.setImage(fiximg)
    # keep track of which components have finished
    feedbackComponents = [image_bac_2, msg_response, fixation_img]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_bac_2* updates
        if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_bac_2.frameNStart = frameN  # exact frame index
            image_bac_2.tStart = t  # local t and not account for scr refresh
            image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_bac_2.started')
            image_bac_2.setAutoDraw(True)
        if image_bac_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                image_bac_2.tStop = t  # not accounting for scr refresh
                image_bac_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                image_bac_2.setAutoDraw(False)
        
        # *msg_response* updates
        if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            msg_response.frameNStart = frameN  # exact frame index
            msg_response.tStart = t  # local t and not account for scr refresh
            msg_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'msg_response.started')
            msg_response.setAutoDraw(True)
        if msg_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                msg_response.tStop = t  # not accounting for scr refresh
                msg_response.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.stopped')
                msg_response.setAutoDraw(False)
        
        # *fixation_img* updates
        if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_img.frameNStart = frameN  # exact frame index
            fixation_img.tStart = t  # local t and not account for scr refresh
            fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_img.started')
            fixation_img.setAutoDraw(True)
        if fixation_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_img.tStop = t  # not accounting for scr refresh
                fixation_img.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                fixation_img.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 20.0 repeats of 'condition5'


# --- Prepare to start Routine "prepare" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from anslist_code
# set environment
numcount = 1
piccenpos_cr = [166, 0, -166]
piccenpos_ar = [166, 0, -166]

# select condition
condition = conditions.pop()
n, image_list, fixation_list = condition

# add condition details to data document
condi = {
    'n=': n,
    'len=': len(image_list),
    'fix=': len(fixation_list)
}
thisExp.addData('condition', condi)
print('N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list),len(conditions))

# analyze the image list
pre_img = []
rom_imgs = image_list.copy()
for _ in range(n):
    temp = random.choice(rom_imgs)
    pre_img.append(temp)
    rom_imgs.remove(temp)

# 生成匹配刺激列表 match_list
match_list = []
ram = range(9 * n)
for _ in ram:
    match_image = random.choice(image_list)
    match_list.append([match_image, match_image])
for item in match_list:
    temp = image_list.copy()
    n1 = n
    while n1 > 1:
        temp.remove(item[n - n1])
        item.insert(n - n1 + 1, random.choice(temp))
        n1 -= 1

# 生成刺激列表 stim_list
stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
while remaining > 0:
    new_image = random.choice(image_list)
    index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
    if index < n:
        stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
        remaining -= 1
    elif index < len(stim_list_pre):
        prev_image = stim_list_pre[index - n][0]
        next_image = stim_list_pre[index][0]

        if new_image != prev_image and new_image != next_image:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
    else:
        if new_image != stim_list_pre[index - n][0]:
            stim_list_pre.insert(index, [new_image])
            remaining -= 1

stim_list = []
# 迭代遍历原始刺激列表拆包
for stim in stim_list_pre:
    if len(stim) > 1:  # 成对的元素
        for s in stim:
            stim_list.append(s)
    else:  # 单个元素
        stim_list.append(stim[0])

# 计算转换后列表中的元素数量
num_elements = len(stim_list)

# 复制 stim_list 生成 answer_list
answer_list = []

if n == 1:
    preimg_list=['01.png']
else:
    preimg_list=['01.png','02.png']
    
allimg_list = preimg_list + stim_list
#anscount = 0
for i in range(n, len(allimg_list)):
    if allimg_list[i] == allimg_list[i - n]:
        answer_list.append('f')
        #anscount += 1
    else:
        answer_list.append('j')
        
if n == 1:
    ncolor = 'yellow'
    ntext = '-1-'
else :
    ncolor = 'purple'
    ntext = '-2-'
    
#print("before experiment stim_list:", stim_list)
#print("before experiment answer_list:",answer_list)
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
pic_01png_2.setImage('01.png')
pic_02png_2.setImage('02.png')
# keep track of which components have finished
prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
for thisComponent in prepareComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "prepare" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_6.started')
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *ins_1back* updates
    if ins_1back.status == NOT_STARTED and n ==1:
        # keep track of start time/frame for later
        ins_1back.frameNStart = frameN  # exact frame index
        ins_1back.tStart = t  # local t and not account for scr refresh
        ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ins_1back.started')
        ins_1back.setAutoDraw(True)
    
    # *ins_2back* updates
    if ins_2back.status == NOT_STARTED and n ==2:
        # keep track of start time/frame for later
        ins_2back.frameNStart = frameN  # exact frame index
        ins_2back.tStart = t  # local t and not account for scr refresh
        ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ins_2back.started')
        ins_2back.setAutoDraw(True)
    
    # *pic_01png_2* updates
    if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        pic_01png_2.frameNStart = frameN  # exact frame index
        pic_01png_2.tStart = t  # local t and not account for scr refresh
        pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pic_01png_2.started')
        pic_01png_2.setAutoDraw(True)
    
    # *pic_02png_2* updates
    if pic_02png_2.status == NOT_STARTED and n == 2:
        # keep track of start time/frame for later
        pic_02png_2.frameNStart = frameN  # exact frame index
        pic_02png_2.tStart = t  # local t and not account for scr refresh
        pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pic_02png_2.started')
        pic_02png_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "prepare" ---
for thisComponent in prepareComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "prepare" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
condition6 = data.TrialHandler(nReps=20.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='condition6')
thisExp.addLoop(condition6)  # add the loop to the experiment
thisCondition6 = condition6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCondition6.rgb)
if thisCondition6 != None:
    for paramName in thisCondition6:
        exec('{} = thisCondition6[paramName]'.format(paramName))

for thisCondition6 in condition6:
    currentLoop = condition6
    # abbreviate parameter names if possible (e.g. rgb = thisCondition6.rgb)
    if thisCondition6 != None:
        for paramName in thisCondition6:
            exec('{} = thisCondition6[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Stim" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_exe
    this_number = numcount
    this_image = stim_list[numcount-1]
    response = ''
    #the central position of picture
    shuffle(piccenpos_cr)
    shuffle(piccenpos_ar)
    piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
    
    ans = answer_list[numcount-1]
    thisExp.addData('ans', ans)
    print("begin routine ","count",numcount,"img",this_image,"ans",ans)
    
    if key_resp_2.corr:
        response = True
    
    else : 
        response = False
    
    
    n_value.setColor(ncolor, colorSpace='rgb')
    n_value.setText(ntext)
    testnum.setText(this_number)
    thisimage.setPos(piccenpos)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    sound_true.setSound('A', secs=0.1, hamming=True)
    sound_true.setVolume(2.0, log=False)
    sound_false.setSound('B', secs=0.2, hamming=False)
    sound_false.setVolume(4.0, log=False)
    # keep track of which components have finished
    StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
    for thisComponent in StimComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Stim" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_bac* updates
        if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_bac.frameNStart = frameN  # exact frame index
            image_bac.tStart = t  # local t and not account for scr refresh
            image_bac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_bac.started')
            image_bac.setAutoDraw(True)
        
        # *n_value* updates
        if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            n_value.frameNStart = frameN  # exact frame index
            n_value.tStart = t  # local t and not account for scr refresh
            n_value.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
            n_value.setAutoDraw(True)
        
        # *num* updates
        if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            num.frameNStart = frameN  # exact frame index
            num.tStart = t  # local t and not account for scr refresh
            num.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
            num.setAutoDraw(True)
        
        # *testnum* updates
        if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            testnum.frameNStart = frameN  # exact frame index
            testnum.tStart = t  # local t and not account for scr refresh
            testnum.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
            testnum.setAutoDraw(True)
        
        # *thisimage* updates
        if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            thisimage.frameNStart = frameN  # exact frame index
            thisimage.tStart = t  # local t and not account for scr refresh
            thisimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
            thisimage.setAutoDraw(True)
        if thisimage.status == STARTED:  # only update if drawing
            thisimage.setImage(this_image, log=False)
        
        # *key_resp_2* updates
        if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            key_resp_2.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = key_resp_2.getKeys(keyList=['f','j'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                key_resp_2.rt = _key_resp_2_allKeys[0].rt
                # was this correct?
                if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_true
        if sound_true.status == NOT_STARTED and response==True:
            # keep track of start time/frame for later
            sound_true.frameNStart = frameN  # exact frame index
            sound_true.tStart = t  # local t and not account for scr refresh
            sound_true.tStartRefresh = tThisFlipGlobal  # on global time
            sound_true.play(when=win)  # sync with win flip
        if sound_true.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                sound_true.tStop = t  # not accounting for scr refresh
                sound_true.frameNStop = frameN  # exact frame index
                sound_true.stop()
        # start/stop sound_false
        if sound_false.status == NOT_STARTED and response==False:
            # keep track of start time/frame for later
            sound_false.frameNStart = frameN  # exact frame index
            sound_false.tStart = t  # local t and not account for scr refresh
            sound_false.tStartRefresh = tThisFlipGlobal  # on global time
            sound_false.play(when=win)  # sync with win flip
        if sound_false.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                sound_false.tStop = t  # not accounting for scr refresh
                sound_false.frameNStop = frameN  # exact frame index
                sound_false.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Stim" ---
    for thisComponent in StimComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_exe
    numcount += 1
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(ans).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for condition6 (TrialHandler)
    condition6.addData('key_resp_2.keys',key_resp_2.keys)
    condition6.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        condition6.addData('key_resp_2.rt', key_resp_2.rt)
    sound_true.stop()  # ensure sound has stopped at end of routine
    sound_false.stop()  # ensure sound has stopped at end of routine
    # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    shuffle(fixation_list)
    fiximg = fixation_list[0]
    
    
    #监听按键信息并给出反馈
    if key_resp_2.corr:
        response = True
        msg = '答对了!'
        msgcolor = 'green'
    
    else : 
        response = False
        msg = '答错了!'
        msgcolor = 'red'
    
    
    
    msg_response.setColor(msgcolor, colorSpace='rgb')
    msg_response.setText(msg)
    fixation_img.setImage(fiximg)
    # keep track of which components have finished
    feedbackComponents = [image_bac_2, msg_response, fixation_img]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_bac_2* updates
        if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_bac_2.frameNStart = frameN  # exact frame index
            image_bac_2.tStart = t  # local t and not account for scr refresh
            image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_bac_2.started')
            image_bac_2.setAutoDraw(True)
        if image_bac_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                image_bac_2.tStop = t  # not accounting for scr refresh
                image_bac_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                image_bac_2.setAutoDraw(False)
        
        # *msg_response* updates
        if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            msg_response.frameNStart = frameN  # exact frame index
            msg_response.tStart = t  # local t and not account for scr refresh
            msg_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'msg_response.started')
            msg_response.setAutoDraw(True)
        if msg_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                msg_response.tStop = t  # not accounting for scr refresh
                msg_response.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.stopped')
                msg_response.setAutoDraw(False)
        
        # *fixation_img* updates
        if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_img.frameNStart = frameN  # exact frame index
            fixation_img.tStart = t  # local t and not account for scr refresh
            fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_img.started')
            fixation_img.setAutoDraw(True)
        if fixation_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_img.tStop = t  # not accounting for scr refresh
                fixation_img.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                fixation_img.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 20.0 repeats of 'condition6'


# --- Prepare to start Routine "prepare" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from anslist_code
# set environment
numcount = 1
piccenpos_cr = [166, 0, -166]
piccenpos_ar = [166, 0, -166]

# select condition
condition = conditions.pop()
n, image_list, fixation_list = condition

# add condition details to data document
condi = {
    'n=': n,
    'len=': len(image_list),
    'fix=': len(fixation_list)
}
thisExp.addData('condition', condi)
print('N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list),len(conditions))

# analyze the image list
pre_img = []
rom_imgs = image_list.copy()
for _ in range(n):
    temp = random.choice(rom_imgs)
    pre_img.append(temp)
    rom_imgs.remove(temp)

# 生成匹配刺激列表 match_list
match_list = []
ram = range(9 * n)
for _ in ram:
    match_image = random.choice(image_list)
    match_list.append([match_image, match_image])
for item in match_list:
    temp = image_list.copy()
    n1 = n
    while n1 > 1:
        temp.remove(item[n - n1])
        item.insert(n - n1 + 1, random.choice(temp))
        n1 -= 1

# 生成刺激列表 stim_list
stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
while remaining > 0:
    new_image = random.choice(image_list)
    index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
    if index < n:
        stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
        remaining -= 1
    elif index < len(stim_list_pre):
        prev_image = stim_list_pre[index - n][0]
        next_image = stim_list_pre[index][0]

        if new_image != prev_image and new_image != next_image:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
    else:
        if new_image != stim_list_pre[index - n][0]:
            stim_list_pre.insert(index, [new_image])
            remaining -= 1

stim_list = []
# 迭代遍历原始刺激列表拆包
for stim in stim_list_pre:
    if len(stim) > 1:  # 成对的元素
        for s in stim:
            stim_list.append(s)
    else:  # 单个元素
        stim_list.append(stim[0])

# 计算转换后列表中的元素数量
num_elements = len(stim_list)

# 复制 stim_list 生成 answer_list
answer_list = []

if n == 1:
    preimg_list=['01.png']
else:
    preimg_list=['01.png','02.png']
    
allimg_list = preimg_list + stim_list
#anscount = 0
for i in range(n, len(allimg_list)):
    if allimg_list[i] == allimg_list[i - n]:
        answer_list.append('f')
        #anscount += 1
    else:
        answer_list.append('j')
        
if n == 1:
    ncolor = 'yellow'
    ntext = '-1-'
else :
    ncolor = 'purple'
    ntext = '-2-'
    
#print("before experiment stim_list:", stim_list)
#print("before experiment answer_list:",answer_list)
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
pic_01png_2.setImage('01.png')
pic_02png_2.setImage('02.png')
# keep track of which components have finished
prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
for thisComponent in prepareComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "prepare" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_6.started')
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *ins_1back* updates
    if ins_1back.status == NOT_STARTED and n ==1:
        # keep track of start time/frame for later
        ins_1back.frameNStart = frameN  # exact frame index
        ins_1back.tStart = t  # local t and not account for scr refresh
        ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ins_1back.started')
        ins_1back.setAutoDraw(True)
    
    # *ins_2back* updates
    if ins_2back.status == NOT_STARTED and n ==2:
        # keep track of start time/frame for later
        ins_2back.frameNStart = frameN  # exact frame index
        ins_2back.tStart = t  # local t and not account for scr refresh
        ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ins_2back.started')
        ins_2back.setAutoDraw(True)
    
    # *pic_01png_2* updates
    if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        pic_01png_2.frameNStart = frameN  # exact frame index
        pic_01png_2.tStart = t  # local t and not account for scr refresh
        pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pic_01png_2.started')
        pic_01png_2.setAutoDraw(True)
    
    # *pic_02png_2* updates
    if pic_02png_2.status == NOT_STARTED and n == 2:
        # keep track of start time/frame for later
        pic_02png_2.frameNStart = frameN  # exact frame index
        pic_02png_2.tStart = t  # local t and not account for scr refresh
        pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pic_02png_2.started')
        pic_02png_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "prepare" ---
for thisComponent in prepareComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "prepare" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
condition7 = data.TrialHandler(nReps=20.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='condition7')
thisExp.addLoop(condition7)  # add the loop to the experiment
thisCondition7 = condition7.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCondition7.rgb)
if thisCondition7 != None:
    for paramName in thisCondition7:
        exec('{} = thisCondition7[paramName]'.format(paramName))

for thisCondition7 in condition7:
    currentLoop = condition7
    # abbreviate parameter names if possible (e.g. rgb = thisCondition7.rgb)
    if thisCondition7 != None:
        for paramName in thisCondition7:
            exec('{} = thisCondition7[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Stim" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_exe
    this_number = numcount
    this_image = stim_list[numcount-1]
    response = ''
    #the central position of picture
    shuffle(piccenpos_cr)
    shuffle(piccenpos_ar)
    piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
    
    ans = answer_list[numcount-1]
    thisExp.addData('ans', ans)
    print("begin routine ","count",numcount,"img",this_image,"ans",ans)
    
    if key_resp_2.corr:
        response = True
    
    else : 
        response = False
    
    
    n_value.setColor(ncolor, colorSpace='rgb')
    n_value.setText(ntext)
    testnum.setText(this_number)
    thisimage.setPos(piccenpos)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    sound_true.setSound('A', secs=0.1, hamming=True)
    sound_true.setVolume(2.0, log=False)
    sound_false.setSound('B', secs=0.2, hamming=False)
    sound_false.setVolume(4.0, log=False)
    # keep track of which components have finished
    StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
    for thisComponent in StimComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Stim" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_bac* updates
        if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_bac.frameNStart = frameN  # exact frame index
            image_bac.tStart = t  # local t and not account for scr refresh
            image_bac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_bac.started')
            image_bac.setAutoDraw(True)
        
        # *n_value* updates
        if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            n_value.frameNStart = frameN  # exact frame index
            n_value.tStart = t  # local t and not account for scr refresh
            n_value.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
            n_value.setAutoDraw(True)
        
        # *num* updates
        if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            num.frameNStart = frameN  # exact frame index
            num.tStart = t  # local t and not account for scr refresh
            num.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
            num.setAutoDraw(True)
        
        # *testnum* updates
        if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            testnum.frameNStart = frameN  # exact frame index
            testnum.tStart = t  # local t and not account for scr refresh
            testnum.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
            testnum.setAutoDraw(True)
        
        # *thisimage* updates
        if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            thisimage.frameNStart = frameN  # exact frame index
            thisimage.tStart = t  # local t and not account for scr refresh
            thisimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
            thisimage.setAutoDraw(True)
        if thisimage.status == STARTED:  # only update if drawing
            thisimage.setImage(this_image, log=False)
        
        # *key_resp_2* updates
        if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            key_resp_2.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = key_resp_2.getKeys(keyList=['f','j'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                key_resp_2.rt = _key_resp_2_allKeys[0].rt
                # was this correct?
                if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_true
        if sound_true.status == NOT_STARTED and response==True:
            # keep track of start time/frame for later
            sound_true.frameNStart = frameN  # exact frame index
            sound_true.tStart = t  # local t and not account for scr refresh
            sound_true.tStartRefresh = tThisFlipGlobal  # on global time
            sound_true.play(when=win)  # sync with win flip
        if sound_true.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                sound_true.tStop = t  # not accounting for scr refresh
                sound_true.frameNStop = frameN  # exact frame index
                sound_true.stop()
        # start/stop sound_false
        if sound_false.status == NOT_STARTED and response==False:
            # keep track of start time/frame for later
            sound_false.frameNStart = frameN  # exact frame index
            sound_false.tStart = t  # local t and not account for scr refresh
            sound_false.tStartRefresh = tThisFlipGlobal  # on global time
            sound_false.play(when=win)  # sync with win flip
        if sound_false.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                sound_false.tStop = t  # not accounting for scr refresh
                sound_false.frameNStop = frameN  # exact frame index
                sound_false.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Stim" ---
    for thisComponent in StimComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_exe
    numcount += 1
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(ans).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for condition7 (TrialHandler)
    condition7.addData('key_resp_2.keys',key_resp_2.keys)
    condition7.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        condition7.addData('key_resp_2.rt', key_resp_2.rt)
    sound_true.stop()  # ensure sound has stopped at end of routine
    sound_false.stop()  # ensure sound has stopped at end of routine
    # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    shuffle(fixation_list)
    fiximg = fixation_list[0]
    
    
    #监听按键信息并给出反馈
    if key_resp_2.corr:
        response = True
        msg = '答对了!'
        msgcolor = 'green'
    
    else : 
        response = False
        msg = '答错了!'
        msgcolor = 'red'
    
    
    
    msg_response.setColor(msgcolor, colorSpace='rgb')
    msg_response.setText(msg)
    fixation_img.setImage(fiximg)
    # keep track of which components have finished
    feedbackComponents = [image_bac_2, msg_response, fixation_img]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_bac_2* updates
        if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_bac_2.frameNStart = frameN  # exact frame index
            image_bac_2.tStart = t  # local t and not account for scr refresh
            image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_bac_2.started')
            image_bac_2.setAutoDraw(True)
        if image_bac_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                image_bac_2.tStop = t  # not accounting for scr refresh
                image_bac_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                image_bac_2.setAutoDraw(False)
        
        # *msg_response* updates
        if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            msg_response.frameNStart = frameN  # exact frame index
            msg_response.tStart = t  # local t and not account for scr refresh
            msg_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'msg_response.started')
            msg_response.setAutoDraw(True)
        if msg_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                msg_response.tStop = t  # not accounting for scr refresh
                msg_response.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.stopped')
                msg_response.setAutoDraw(False)
        
        # *fixation_img* updates
        if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_img.frameNStart = frameN  # exact frame index
            fixation_img.tStart = t  # local t and not account for scr refresh
            fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_img.started')
            fixation_img.setAutoDraw(True)
        if fixation_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_img.tStop = t  # not accounting for scr refresh
                fixation_img.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                fixation_img.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 20.0 repeats of 'condition7'


# --- Prepare to start Routine "prepare" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from anslist_code
# set environment
numcount = 1
piccenpos_cr = [166, 0, -166]
piccenpos_ar = [166, 0, -166]

# select condition
condition = conditions.pop()
n, image_list, fixation_list = condition

# add condition details to data document
condi = {
    'n=': n,
    'len=': len(image_list),
    'fix=': len(fixation_list)
}
thisExp.addData('condition', condi)
print('N值', n, '图表长度', len(image_list), '注视点表长度', len(fixation_list),len(conditions))

# analyze the image list
pre_img = []
rom_imgs = image_list.copy()
for _ in range(n):
    temp = random.choice(rom_imgs)
    pre_img.append(temp)
    rom_imgs.remove(temp)

# 生成匹配刺激列表 match_list
match_list = []
ram = range(9 * n)
for _ in ram:
    match_image = random.choice(image_list)
    match_list.append([match_image, match_image])
for item in match_list:
    temp = image_list.copy()
    n1 = n
    while n1 > 1:
        temp.remove(item[n - n1])
        item.insert(n - n1 + 1, random.choice(temp))
        n1 -= 1

# 生成刺激列表 stim_list
stim_list_pre = match_list.copy()  # 复制匹配刺激列表作为基础
remaining = 45 - len(match_list) * (n + 1)  # 剩余待插入元素的数量
while remaining > 0:
    new_image = random.choice(image_list)
    index = random.randint(0, len(stim_list_pre))  # 随机选择插入位置
    if index < n:
        stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
        remaining -= 1
    elif index < len(stim_list_pre):
        prev_image = stim_list_pre[index - n][0]
        next_image = stim_list_pre[index][0]

        if new_image != prev_image and new_image != next_image:
            stim_list_pre.insert(index, [new_image])  # 在选择的位置插入新元素
            remaining -= 1
    else:
        if new_image != stim_list_pre[index - n][0]:
            stim_list_pre.insert(index, [new_image])
            remaining -= 1

stim_list = []
# 迭代遍历原始刺激列表拆包
for stim in stim_list_pre:
    if len(stim) > 1:  # 成对的元素
        for s in stim:
            stim_list.append(s)
    else:  # 单个元素
        stim_list.append(stim[0])

# 计算转换后列表中的元素数量
num_elements = len(stim_list)

# 复制 stim_list 生成 answer_list
answer_list = []

if n == 1:
    preimg_list=['01.png']
else:
    preimg_list=['01.png','02.png']
    
allimg_list = preimg_list + stim_list
#anscount = 0
for i in range(n, len(allimg_list)):
    if allimg_list[i] == allimg_list[i - n]:
        answer_list.append('f')
        #anscount += 1
    else:
        answer_list.append('j')
        
if n == 1:
    ncolor = 'yellow'
    ntext = '-1-'
else :
    ncolor = 'purple'
    ntext = '-2-'
    
#print("before experiment stim_list:", stim_list)
#print("before experiment answer_list:",answer_list)
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
pic_01png_2.setImage('01.png')
pic_02png_2.setImage('02.png')
# keep track of which components have finished
prepareComponents = [key_resp_6, ins_1back, ins_2back, pic_01png_2, pic_02png_2]
for thisComponent in prepareComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "prepare" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_6.started')
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *ins_1back* updates
    if ins_1back.status == NOT_STARTED and n ==1:
        # keep track of start time/frame for later
        ins_1back.frameNStart = frameN  # exact frame index
        ins_1back.tStart = t  # local t and not account for scr refresh
        ins_1back.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_1back, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ins_1back.started')
        ins_1back.setAutoDraw(True)
    
    # *ins_2back* updates
    if ins_2back.status == NOT_STARTED and n ==2:
        # keep track of start time/frame for later
        ins_2back.frameNStart = frameN  # exact frame index
        ins_2back.tStart = t  # local t and not account for scr refresh
        ins_2back.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_2back, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ins_2back.started')
        ins_2back.setAutoDraw(True)
    
    # *pic_01png_2* updates
    if pic_01png_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        pic_01png_2.frameNStart = frameN  # exact frame index
        pic_01png_2.tStart = t  # local t and not account for scr refresh
        pic_01png_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic_01png_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pic_01png_2.started')
        pic_01png_2.setAutoDraw(True)
    
    # *pic_02png_2* updates
    if pic_02png_2.status == NOT_STARTED and n == 2:
        # keep track of start time/frame for later
        pic_02png_2.frameNStart = frameN  # exact frame index
        pic_02png_2.tStart = t  # local t and not account for scr refresh
        pic_02png_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pic_02png_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'pic_02png_2.started')
        pic_02png_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "prepare" ---
for thisComponent in prepareComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "prepare" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
condition8 = data.TrialHandler(nReps=20.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='condition8')
thisExp.addLoop(condition8)  # add the loop to the experiment
thisCondition8 = condition8.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCondition8.rgb)
if thisCondition8 != None:
    for paramName in thisCondition8:
        exec('{} = thisCondition8[paramName]'.format(paramName))

for thisCondition8 in condition8:
    currentLoop = condition8
    # abbreviate parameter names if possible (e.g. rgb = thisCondition8.rgb)
    if thisCondition8 != None:
        for paramName in thisCondition8:
            exec('{} = thisCondition8[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Stim" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_exe
    this_number = numcount
    this_image = stim_list[numcount-1]
    response = ''
    #the central position of picture
    shuffle(piccenpos_cr)
    shuffle(piccenpos_ar)
    piccenpos = (piccenpos_cr[0], piccenpos_ar[0])
    
    ans = answer_list[numcount-1]
    thisExp.addData('ans', ans)
    print("begin routine ","count",numcount,"img",this_image,"ans",ans)
    
    if key_resp_2.corr:
        response = True
    
    else : 
        response = False
    
    
    n_value.setColor(ncolor, colorSpace='rgb')
    n_value.setText(ntext)
    testnum.setText(this_number)
    thisimage.setPos(piccenpos)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    sound_true.setSound('A', secs=0.1, hamming=True)
    sound_true.setVolume(2.0, log=False)
    sound_false.setSound('B', secs=0.2, hamming=False)
    sound_false.setVolume(4.0, log=False)
    # keep track of which components have finished
    StimComponents = [image_bac, n_value, num, testnum, thisimage, key_resp_2, sound_true, sound_false]
    for thisComponent in StimComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Stim" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_bac* updates
        if image_bac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_bac.frameNStart = frameN  # exact frame index
            image_bac.tStart = t  # local t and not account for scr refresh
            image_bac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_bac, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_bac.started')
            image_bac.setAutoDraw(True)
        
        # *n_value* updates
        if n_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            n_value.frameNStart = frameN  # exact frame index
            n_value.tStart = t  # local t and not account for scr refresh
            n_value.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(n_value, 'tStartRefresh')  # time at next scr refresh
            n_value.setAutoDraw(True)
        
        # *num* updates
        if num.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            num.frameNStart = frameN  # exact frame index
            num.tStart = t  # local t and not account for scr refresh
            num.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(num, 'tStartRefresh')  # time at next scr refresh
            num.setAutoDraw(True)
        
        # *testnum* updates
        if testnum.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            testnum.frameNStart = frameN  # exact frame index
            testnum.tStart = t  # local t and not account for scr refresh
            testnum.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testnum, 'tStartRefresh')  # time at next scr refresh
            testnum.setAutoDraw(True)
        
        # *thisimage* updates
        if thisimage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            thisimage.frameNStart = frameN  # exact frame index
            thisimage.tStart = t  # local t and not account for scr refresh
            thisimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thisimage, 'tStartRefresh')  # time at next scr refresh
            thisimage.setAutoDraw(True)
        if thisimage.status == STARTED:  # only update if drawing
            thisimage.setImage(this_image, log=False)
        
        # *key_resp_2* updates
        if key_resp_2.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            key_resp_2.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = key_resp_2.getKeys(keyList=['f','j'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                key_resp_2.rt = _key_resp_2_allKeys[0].rt
                # was this correct?
                if (key_resp_2.keys == str(ans)) or (key_resp_2.keys == ans):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_true
        if sound_true.status == NOT_STARTED and response==True:
            # keep track of start time/frame for later
            sound_true.frameNStart = frameN  # exact frame index
            sound_true.tStart = t  # local t and not account for scr refresh
            sound_true.tStartRefresh = tThisFlipGlobal  # on global time
            sound_true.play(when=win)  # sync with win flip
        if sound_true.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_true.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                sound_true.tStop = t  # not accounting for scr refresh
                sound_true.frameNStop = frameN  # exact frame index
                sound_true.stop()
        # start/stop sound_false
        if sound_false.status == NOT_STARTED and response==False:
            # keep track of start time/frame for later
            sound_false.frameNStart = frameN  # exact frame index
            sound_false.tStart = t  # local t and not account for scr refresh
            sound_false.tStartRefresh = tThisFlipGlobal  # on global time
            sound_false.play(when=win)  # sync with win flip
        if sound_false.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_false.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                sound_false.tStop = t  # not accounting for scr refresh
                sound_false.frameNStop = frameN  # exact frame index
                sound_false.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StimComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Stim" ---
    for thisComponent in StimComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_exe
    numcount += 1
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(ans).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for condition8 (TrialHandler)
    condition8.addData('key_resp_2.keys',key_resp_2.keys)
    condition8.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        condition8.addData('key_resp_2.rt', key_resp_2.rt)
    sound_true.stop()  # ensure sound has stopped at end of routine
    sound_false.stop()  # ensure sound has stopped at end of routine
    # the Routine "Stim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_code
    shuffle(fixation_list)
    fiximg = fixation_list[0]
    
    
    #监听按键信息并给出反馈
    if key_resp_2.corr:
        response = True
        msg = '答对了!'
        msgcolor = 'green'
    
    else : 
        response = False
        msg = '答错了!'
        msgcolor = 'red'
    
    
    
    msg_response.setColor(msgcolor, colorSpace='rgb')
    msg_response.setText(msg)
    fixation_img.setImage(fiximg)
    # keep track of which components have finished
    feedbackComponents = [image_bac_2, msg_response, fixation_img]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_bac_2* updates
        if image_bac_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_bac_2.frameNStart = frameN  # exact frame index
            image_bac_2.tStart = t  # local t and not account for scr refresh
            image_bac_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_bac_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_bac_2.started')
            image_bac_2.setAutoDraw(True)
        if image_bac_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_bac_2.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                image_bac_2.tStop = t  # not accounting for scr refresh
                image_bac_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_bac_2.stopped')
                image_bac_2.setAutoDraw(False)
        
        # *msg_response* updates
        if msg_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            msg_response.frameNStart = frameN  # exact frame index
            msg_response.tStart = t  # local t and not account for scr refresh
            msg_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(msg_response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'msg_response.started')
            msg_response.setAutoDraw(True)
        if msg_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > msg_response.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                msg_response.tStop = t  # not accounting for scr refresh
                msg_response.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msg_response.stopped')
                msg_response.setAutoDraw(False)
        
        # *fixation_img* updates
        if fixation_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_img.frameNStart = frameN  # exact frame index
            fixation_img.tStart = t  # local t and not account for scr refresh
            fixation_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_img.started')
            fixation_img.setAutoDraw(True)
        if fixation_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_img.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_img.tStop = t  # not accounting for scr refresh
                fixation_img.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_img.stopped')
                fixation_img.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 20.0 repeats of 'condition8'


# --- Prepare to start Routine "thanks" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
thanksComponents = [text_3, key_resp_3]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "thanks" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        text_3.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3.started')
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "thanks" ---
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
