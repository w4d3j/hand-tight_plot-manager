import getopt
import glob
import os
import sys
from pathlib import Path
from subprocess import Popen


class Bitch:
    def __init__(bitch, name):
        o = 'old'
        bitch.name = name
        bitch.path = Path('/home/wade/x')
        bitch.opath = bitch.path / o

    @property
    def plots(bitch):
        n = 'new'
        o = 'old'
        d = 'del'
        retplots = []
        retoplots = []
        for plot in bitch.path.glob("*.plot"):
            retplots.append(plot)
        for oplot in bitch.opath.glob("*.plot"):
            retoplots.append(oplot)
        return {n: retplots, o: retoplots, d: retoplots[:4]}

    @property
    def numplots(bitch):
        n = 'new'
        o = 'old'
        t = 'total'
        nnew = len(bitch.plots[n])
        nold = len(bitch.plots[o])
        ntot = nnew + nold
        return {n: nnew, o: nold, t: ntot}

    @property
    def disk_(bitch):
        t = 'total'
        f = 'free'
        u = 'used'
        disk = os.statvfs(bitch.path)
        totalgigs = (disk.f_frsize *
                     disk.f_blocks) / (float(1 << 30))
        usedgigs = ((disk.f_frsize -
                     disk.f_bfree) *
                    disk.f_blocks) / (float(1 << 30))
        freegigs = (disk.f_frsize *
                    disk.f_bfree) / (float(1 << 30))
        return {t: totalgigs, u: usedgigs, f: freegigs}


def shitmove():
    bitchlist = []
    old = Bitch('oldbitch')
    # ugly = Bitch('uglybitch')
    lazy = Bitch('lazybitch')
    little = Bitch('littlebitch')
    # punk = Bitch('punkbitch')
    # psycho = Bitch('psychobitch')
    # stuckup = Bitch('stuckupbitch')
    # nosy = Bitch('nosybitch')
    nasty = Bitch('nastybitch')
    stanky = Bitch('stankybitch')

    bitchlist = [lazy, nasty, little, stanky, old]

    o = 'old'
    f = 'free'
    d = 'del'
    alpha = []
    beta = []
    gamma = []
    delta = []
    omega = []

    for i in range(len(bitchlist)):
        print('Bitchlist includes: {0}'.format(bitchlist))
        thisbitch = bitchlist[i]
        if thisbitch.disk_[f] > 456:
            alpha.append(thisbitch)
            print('''added {} to ALPHA list, it has plenty of room, \
                {} total'''.format(thisbitch.name, len(alpha)))
        elif thisbitch.numplots[o] > 3:
            beta.append(thisbitch)
            print('''added {} to BETA list because we can make \
                plenty of room by deleting old plots, \
                    {} total'''.format(thisbitch.name, len(beta)))
        elif thisbitch.numplots[o] > 0:
            gamma.append(thisbitch)
            print('''added {} to GAMMA list because we can make \
                a little room by deleting old plots, \
                    {} total'''.format(thisbitch.name, len(gamma)))
        elif thisbitch.disk_[f] >= 102:
            delta.append(thisbitch)
            print('''added {} to DELTA list because there are \
                no more old plots but there is enough \
                    space, {} total'''.format(thisbitch.name, len(delta)))
        else:
            print('IDKWTFIGO')
            type
    if len(alpha) >= 3:
        omega = alpha[:3]
        print('ALPHA had 3+ bitches, scooping them into OMEGA: {0}'.format(omega))
    else:
        omega = alpha
        print('now omega = alpha = {0}'.format(omega))
        epsilon = beta + gamma
        print('epsilon = beta + gamma = {0}'.format(epsilon))
        remains = 3 - len(omega)
        remainingbitches = epsilon[:remains]
        print('pulling {0} bitches from epsilon to fill omega to 3'.format(remainingbitches))
        if len(remainingbitches) > 0:
            for bitch in remainingbitches:
                print('deleting plots {0}'.format(bitch.plots[d]))
                for delplot in bitch.plots[d]:
                    delplot.unlink()
                print('appending {0} to OMEGA'.format(bitch.name))
                omega.append(bitch)
                print('OMEGA is now {0}'.format(omega))
        omega += delta
        print('added delta to OMEGA, now omega is {0}'.format(omega))
    if len(omega) != 3:
        print("Omega has {} entries, figure it out bud".format(len(omega)))
    if len(omega) > 3:
        omega = omega[:3]
        print('trimmed OMEGA to len 3: {0}'.format(omega))
    return omega


def rsyncSE(drivelist):
    if len(drivelist) > 3:
        drivelist = drivelist[:3]
    rs = 'rsync'
    avh = '-avh'
    rsf = '--remove-source-files'
    commands = []
    copyplots = []
    for plot in Path('/home/wade/x/shiteater').glob("*.plot"):
        copyplots.append(str(plot))
        print ('..appended {0} to copyplots'.format(plot))
    for i in range(len(copyplots)):
        todir = str(drivelist[i].path)
        copyplot = copyplots[i]
        command = [rs, avh, rsf, '--progress', copyplot, todir]
        commands.append(command)
        print('..appended command {0} ([rs, avh, rsf, --progress, copyplot, todir]) to commands list'.format(command))
    runningcmds = []
    if len(commands) > 0:
        p1 = Popen(commands[0])
        runningcmds.append(p1)
        print('if len(commands) > 0, p1 = Popen({0}) and append to runningcmds'.format(commands[0]))
    if len(commands) > 1:
        p2 = Popen(commands[1])
        runningcmds.append(p2)
        print('if len(commands) > 1, p2 = Popen({0}) and append to runningcmds'.format(commands[1]))
    if len(commands) > 2:
        p3 = Popen(commands[2])
        runningcmds.append(p3)
        print('if len(commands) > 2, p3 = Popen({0}) and append to runningcmds'.format(commands[2]))
    exitcodes = []
    for p in runningcmds:
        print('Waiting on {0} to finish...'.format(p) )
        exitcodes.append(p.wait())
    return exitcodes


def shitplot():
    bitchdir = Path.home() / 'x'
    dw = str(bitchdir / 'dickweasel')
    tb = str(bitchdir / 'turdburglar')
    se = str(bitchdir / 'shiteater')
    dws = dw + '/'
    tbs = tb + '/'
    fkey = os.environ['FKEY']
    sppk = os.environ['SPPK']
    plotcmd = [
        'chia_plot',
        '-n', '1',
        '-r', '12',
        '-u', '128',
        '-v', '128',
        '-K', '2',
        '-t', tbs,
        '-2', dws,
        '-c', sppk,
        '-f', fkey
        ]
    while True:
        plotter = Popen(plotcmd)
        try:
            turdplot = glob.glob(tbs + "/*.plot")[0]
            turdcmd = ['rsync', '-avh', '--remove-source-files',
                       '--progress', turdplot, se]
        except IndexError:
            turdcmd = ['echo', '''"  |:-:--     NO TURDS TODAY, FOLKS       -:\
|:-       We'll get em next time      --:-:| "''']
        turdcopy = Popen(turdcmd)
        print('Turd command started {0} -- waiting...'.format(turdcmd))
        turdcopy.wait()
        shits = glob.glob(se + "/*.plot")
        if len(shits) >= 3:
            print('Plots found on shiteater, running shitmove and rshytc on {0}'.format(shits))
            weeoo = shitmove()
            print('..shitmove complete: {0}\nStarting rshytc'.format(weeoo))
            rsyncSE(weeoo)
        plotter.wait()


def madplot(say_when=1, shiteating_layover=False):
    bitchdir = Path.home() / 'x'
    dw = str(bitchdir / 'dickweasel/')
    tb = str(bitchdir / 'turdburglar/')
    se = str(bitchdir / 'shiteater/')
    fkey = os.environ['FKEY']
    sppk = os.environ['SPPK']
    if say_when > 5:
        shiteating_layover = True
    d_args = []
    if shiteating_layover == True:
        d_args = ['-d', se]
    mdmx = ['chia_plot',
            '-n', say_when,
            '-r', '12',
            '-u', '128',
            '-v', '128',
            '-K', '2',
            '-t', tb,
            '-2', dw
            ] + d_args + [
            '-c', sppk,
            '-f', fkey]
    madmax = Popen(mdmx)
    madmax.wait()


# madflag = False
# numplots = 1
# layover = False
# optns = getopt.getopt(sys.argv[1:], 'mns', ['solo',
#                                             'mad',
#                                             'madonly',
#                                             'num=',
#                                             'plots=',
#                                             'numplots=',
#                                             'shit',
#                                             'shitlay',
#                                             'eatshit'
#                                             ])
# for opt, arg in optns:
#     if opt in ('-m', '--solo', '--mad', '--madonly'):
#         madflag = True
#     elif opt in ('-n', '--num', '--plots', '--numplots'):
#         numplots = arg
#     elif opt in ('-s', '--shit', '--shitlay', '--eatshit'):
#         layover = True

if __name__ == '__main__':
    # if madflag == True:
    #     madplot(numplots, layover)
    # elif madflag == False:
    shitplot()
