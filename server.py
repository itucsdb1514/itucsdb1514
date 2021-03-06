import datetime
import json
import os
import re

from flask import Flask
from flask import render_template,request,url_for,redirect
from pages import HomePage,initPage,sponsorslist, playerslist, teamslist, stadiumslist, commentslist, coacheslist, natslist, matcheslist, userslist,leagueslist, statslist
from pages import PHDetail,outfitPage ,likeslist, betrateslist


app = Flask(__name__)


@app.route('/')
def home():
    return HomePage.HomePageFunc()

@app.route('/initDB/')
def InitDb():
    return initPage.InitPageFunc(app.config['dsn'])

@app.route('/sponsorsList', methods=['GET', 'POST'])
def sponsorsList():
    dsn=app.config['dsn']
    return sponsorslist.sponsorsList(dsn)
@app.route('/sponsorsList/Update', methods=['GET', 'POST'])
def sponsorsListUpdate():
    dsn=app.config['dsn']
    return sponsorslist.sponsorsListUpdate(dsn)

@app.route('/stadiumsList', methods=['GET', 'POST'])
def stadiumsList():
    dsn=app.config['dsn']
    return stadiumslist.stadiumsList(dsn)

@app.route('/stadiumsList/Update', methods=['GET', 'POST'])
def stadiumsListUpdate():
    dsn=app.config['dsn']
    return stadiumslist.updateStadiumsList(dsn)

@app.route('/matchesList/', methods=['GET', 'POST'])
def matchesList():
    dsn=app.config['dsn']
    return matcheslist.matchesList(dsn)

@app.route('/matchesList/Update', methods=['GET', 'POST'])
def matchesListUpdate():
    dsn=app.config['dsn']
    return matcheslist.updateMatchesList(dsn)

@app.route('/betratesList/', methods=['GET', 'POST'])
def betratesList():
    dsn=app.config['dsn']
    return betrateslist.betratesList(dsn)

@app.route('/betratesList/Update', methods=['GET', 'POST'])
def betratesListUpdate():
    dsn=app.config['dsn']
    return betrateslist.updateBetratesList(dsn)

@app.route('/playersList/', methods=['GET', 'POST'])
def playersList():
    dsn=app.config['dsn']
    return playerslist.playersList(dsn)

@app.route('/usersList', methods=['GET', 'POST'])
def usersList():
    dsn=app.config['dsn']
    return userslist.usersList(dsn)

@app.route('/playersList/Update', methods=['GET', 'POST'])
def playersListUpdate():
    dsn=app.config['dsn']
    return playerslist.updatePlayersList(dsn)

@app.route('/usersList/Update', methods=['GET', 'POST'])
def usersListUpdate():
    dsn=app.config['dsn']
    return userslist.updateUsersList(dsn)

@app.route('/natsList', methods=['GET', 'POST'])
def natsList():
    dsn=app.config['dsn']
    return natslist.natsList(dsn)

@app.route('/natsList/Update', methods=['GET', 'POST'])
def natsListUpdate():
    dsn=app.config['dsn']
    return natslist.updateNatsList(dsn)

@app.route('/statsList', methods=['GET', 'POST'])
def statsList():
    dsn=app.config['dsn']
    return statslist.statsList(dsn)

@app.route('/statsList/Update', methods=['GET', 'POST'])
def statsListUpdate():
    dsn=app.config['dsn']
    return statslist.updateStatsList(dsn)


@app.route('/teamsList', methods=['GET', 'POST'])
def teamsList():
    dsn=app.config['dsn']
    return teamslist.teamsList(dsn)

@app.route('/teamsList/Update', methods=['GET', 'POST'])
def teamsListUpdate():
    dsn=app.config['dsn']
    return teamslist.updateTeamsList(dsn)

@app.route('/leaguesList', methods=['GET', 'POST'])
def leaguesList():
    dsn=app.config['dsn']
    return leagueslist.leaguesList(dsn)

@app.route('/leaguesList/Update', methods=['GET', 'POST'])
def leaguesListUpdate():
    dsn=app.config['dsn']
    return leagueslist.updateLeaguesList(dsn)


@app.route('/coachesList', methods=['GET', 'POST'])
def coachesList():
    dsn=app.config['dsn']
    return coacheslist.coachesList(dsn)

@app.route('/coachesList/Update', methods=['GET', 'POST'])
def coachesListUpdate():
    dsn=app.config['dsn']
    return coacheslist.updateCoachesList(dsn)

@app.route('/commentsList', methods=['GET', 'POST'])
def commentsList():
    dsn=app.config['dsn']
    return commentslist.commentsList(dsn)

@app.route('/commentsList/Update', methods=['GET', 'POST'])
def commentsListUpdate():
    dsn=app.config['dsn']
    return commentslist.updateCommentsList(dsn)

@app.route('/playerHistory/<int:id>', methods=['GET', 'POST'])
def playerHistory(id):
    dsn=app.config['dsn']
    return PHDetail.PHDetail(dsn,id)
@app.route('/playerHistory/Update/<int:id>', methods=['GET', 'POST'])
def playerHistoryupdate(id):
    dsn=app.config['dsn']
    return PHDetail.PHDetailUpdate(dsn,id)
@app.route('/outfit/<int:id>', methods=['GET', 'POST'])
def outfitpage(id):
    dsn=app.config['dsn']
    return outfitPage.outfitPage(dsn,id);
@app.route('/outfit/Update/<int:id>', methods=['GET', 'POST'])
def outfitpageUpdate(id):
    dsn=app.config['dsn']
    return outfitPage.outfitPageUpdate(dsn,id);
@app.route('/likesList', methods=['GET', 'POST'])
def likesList():
    dsn=app.config['dsn']
    return likeslist.likesList(dsn)

@app.route('/likesList/Update', methods=['GET', 'POST'])
def likesListUpdate():
    dsn=app.config['dsn']
    return likeslist.updateLikesList(dsn)
def get_elephantsql_dsn(vcap_services):
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
    dbname='{}'""".format(user, password, host, port, dbname)
    return dsn

if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True
    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_elephantsql_dsn(VCAP_SERVICES)
    else:
        app.config['dsn'] =  """host='localhost' port=54321  password='vagrant' user='vagrant' dbname='itucsdb'"""
    app.run(host='0.0.0.0', port=port, debug=debug)
