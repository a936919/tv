D6='Referer'
D5='liveapi2'
D4='playUrl'
D3='mimeType'
D2='codecid'
D1='192000'
D0='media_ft'
C_='media_bangumi'
Cz='stream'
Cy='playurl_info'
Cx='\u3000UID：'
Cw='是否关注$ '
Cv='vod_list'
Cu='\u3000👥 '
Ct='➖取关$2_notplay_follow'
Cs='➕关注$1_notplay_follow'
Cr='bilidanmu'
Cq='setting'
Cp='Reply_jump'
Co='https://b23.tv/'
Cn='message'
Cm='totalrank'
Cl='room_id'
Ck='featured'
Cj='favorite'
Ci='attention'
Ch='\u3000💬'
Cg='videos'
Cf='  个人主页'
Ce='quicksearch'
Cd='oldest'
Cc='user_cover'
Cb='roomid'
Ca='text_small'
CZ='watched_show'
CY='live_status'
CX='offset'
CW='查看直播细化标签'
CV='/index.php/update.json'
CU='fav_list'
CT='https://api.bilibili.com/x/web-interface/nav'
CS='bangumi_pay_parse'
CR='bangumi_vip_parse'
CQ='bangumi_horizontal_cover'
CP='hide_bangumi_vip_badge'
CO='hide_bangumi_preview'
CN='raw_cookie_vip'
CM='raw_cookie_line'
CK='header'
CJ='vodTMPQn'
CI='wts'
CH='csrf'
CG='dur'
CF='playurl'
CE='ver'
CD='checkUpdate'
CC='interaction'
CB='vod_director'
CA='vod_area'
C9='vod_year'
C8='title_type'
C7='000'
C6='bili_user'
C5='sort'
C4='season_status'
C3='all'
C2='special'
C1='悄悄关注'
C0='最近关注'
B_='bangumi'
Bz='coin'
By='like_num'
Bx='part'
Bw='play'
Bv='vod_pc'
Bu='module_author'
Bt='https://www.bilibili.com'
Bs='isVIP'
Br='isLogin'
Bq='https://'
Bp='排行榜'
Bo='showLiveFilterTag'
Bn='vodDefaultCodec'
Bm='favMode'
Bl='maxHomeVideoContent'
Bk='currentVersion'
Bj=round
Be='audio'
Bd='format'
Bc='codec'
Bb='status'
Ba='vod_actor'
BZ='redirect_url'
BY='edgeid'
BX='$ '
BW='BV'
BV='最近访问'
BU='稍后再看'
BT='vod_count'
BS='episodes'
BR='  ▶'
BQ='  💬'
BP='content'
BO='archive'
BN='UP主'
BM='modules'
BL='items'
BK='分区'
BJ='type_name'
BI='搜索'
BH='历史'
BG='关注'
BF='rankingLis'
BE='tuijianLis'
BD='heartbeatInterval'
BC=float
BB=open
BA='contentType'
B9='s_title'
B8='graph_version'
B7='fromep'
B6='ssid'
B5='seasons'
B4='特别关注'
B3='正在直播'
B2='like'
B1='new_ep'
B0='index_show'
A_='view'
Az='danmaku'
Ay='stat'
Ax='pic'
Aw='  🆙'
Av='keyword'
Au='channel_list'
At='userid'
As='utf-8'
Ar='频道'
Aq='cateManual'
Ap='show_vod_hot_reply'
Ao='vodDefaultAudio'
An='vodDefaultQn'
Am='@@@'
Al='season_title'
Ak='parse'
Aj='Reply'
Ai='fans'
Ah='following'
Ag='pubdate'
Af='owner'
Ae='mlid'
Ad='收藏'
Ac='影视'
Ab='vod_content'
Aa='\u3000'
AZ='desc'
AY='up'
AX='season_id'
AW='live'
AV='4'
AU=None
AT='cateLive'
AS='vip'
AR='推荐'
AQ='3'
AP='newVersion'
AO='vod_play_url'
AN='vod_play_from'
AM='result'
AL=' '
AK='"'
AJ='&quot;'
AI='动态'
AH='直播'
AG=True
AE='_tmp'
AD='﹩'
AC='﹟'
AB='video'
AA='/'
A9='User-Agent'
A8='uname'
A7='face'
A6='UP'
A5='cateManualLiveExtra'
A4='cookies_dic'
A3='热门'
A2=dict
A1='tid'
A0='2'
z='ep'
y='cateManualLive'
w='$'
v='av'
u='limit'
t='pagecount'
s=list
r='type'
q='ss'
p='total'
o='url'
n='cid'
m='id'
l='</em>'
k='<em class="keyword">'
i='page'
h='master'
g=map
f='$$$'
e='duration'
d='cover'
c='users'
b='order'
a='aid'
Z='filter'
Y='page_size'
X='vod_remarks'
W=len
V='mid'
U='vod_pic'
T='1'
S='key'
R='title'
Q='vod_id'
P='vod_name'
O='fake'
N='#'
M='code'
L='0'
G='value'
K='name'
J='_'
H='list'
F=int
E='data'
D='n'
C='v'
B=''
A=str
import sys,os,json as I
from base.spider import Spider
from requests import session as Bf,utils as Bg,get as Bh
from requests.adapters import HTTPAdapter as D7,Retry
from concurrent.futures import ThreadPoolExecutor as D8,as_completed as Bi
import threading as j,hashlib,time as x,random
from functools import reduce
from urllib.parse import quote,urlencode as CL
sys.path.append('..')
AF,D9=os.path.split(os.path.abspath(__file__))
sys.path.append(AF)
class Spider(Spider):
	defaultConfig={Bk:'20230523_2',CM:B,CN:B,Bl:AQ,Bm:L,Y:10,BD:'15',An:'80',Bn:'7',Ao:'30280',Ap:AG,CO:AG,CP:AG,CQ:AG,CR:AG,CS:AG,Bo:L,Aq:[AR,Ac,AH,AI,Ar,Ad,BG,BH,BI],BE:[A3,Bp,'每周必看','入站必刷','番剧时间表','国创时间表'],BF:['动画','音乐','舞蹈','游戏','鬼畜','知识','科技','运动','生活','美食','动物','汽车','时尚','娱乐',Ac,'原创','新人']};focus_on_up_list=[];focus_on_search_key=[]
	def getName(A):return'哔哩哔哩'
	def load_config(A):
		try:
			with BB(f"{AF}/config.json",encoding=As)as D:A.userConfig=I.load(D)
			E={h:'cookie_dic',AS:'cookie_vip_dic',O:'cookie_fake_dic'}
			for(F,C)in E.items():
				C=A.userConfig.get(C)
				if C:
					if not A.userConfig.get(c):A.userConfig[c]={}
					A.userConfig[c][F]={A4:C}
			B=A.userConfig.get(c,{})
			if B.get(h)and B[h].get(A4):A.session_master.cookies=Bg.cookiejar_from_dict(B[h][A4]);A.userid=B[h][At]
			if B.get(O)and B[O].get(A4):A.session_fake.cookies=Bg.cookiejar_from_dict(B[O][A4])
		except:A.userConfig={}
		A.userConfig={**A.defaultConfig,**A.userConfig}
	dump_config_lock=j.Lock()
	def dump_config(A):
		F=[c,Au,AT,y,A5];C={}
		for(B,D)in A.userConfig.items():
			E=A.defaultConfig.get(B)
			if E!=AU and D!=E or B in F:C[B]=D
		A.dump_config_lock.acquire()
		with BB(f"{AF}/config.json",'w',encoding=As)as G:H=I.dumps(C,indent=1,ensure_ascii=False);G.write(H)
		A.dump_config_lock.release()
	pool=D8(max_workers=8);task_pool=[]
	def homeContent(A,filter):
		A.pool.submit(A.add_live_filter);A.pool.submit(A.add_channel_filter);A.pool.submit(A.add_search_key);A.pool.submit(A.add_focus_on_up_filter);A.pool.submit(A.get_tuijian_filter);A.pool.submit(A.add_fav_filter);A.pool.submit(A.homeVideoContent);F=[AI,Ad,BG,BH];B=A.userConfig[Aq]
		if not A.userid and not A6 in B or not AI in B and not A6 in B:B+=[A6]
		D=[]
		for C in B:
			if C in F and not A.userid:continue
			D.append({BJ:C,'type_id':C})
		A.add_focus_on_up_filter_event.wait()
		if A6 in B:A.config[Z].update({A6:A.config[Z].pop(AI)})
		E={'class':D};A.add_live_filter_event.wait();A.add_channel_filter_event.wait();A.add_fav_filter_event.wait();A.add_search_key_event.wait()
		if filter:E['filters']=A.config[Z]
		A.pool.submit(A.dump_config);A.pool.submit(A.test_mirror_site);return E
	userid=csrf=B;session_master=Bf();session_vip=Bf();session_fake=Bf();con=j.Condition();getCookie_event=j.Event();retries=Retry(total=5,backoff_factor=.1);adapter=D7(max_retries=retries);session_master.mount(Bq,adapter);session_vip.mount(Bq,adapter);session_fake.mount(Bq,adapter)
	def getCookie_dosth(B,co):
		A=co.strip().split('=',1)
		if not'%'in A[1]:A[1]=quote(A[1])
		return A
	def getCookie(A,_type=h):
		D=_type;G=CM
		if D==AS:G=CN
		G=A.userConfig.get(G);K=A.userConfig.get(c,{});C=K.get(D,{})
		if not G and not C:
			if D==h:A.getCookie_event.set()
			with A.con:A.con.notifyAll()
			return
		J=C.get(A4,{})
		if G:J=A2(g(A.getCookie_dosth,G.split(';')))
		L=Bg.cookiejar_from_dict(J);N=CT;O=A.fetch(N,headers=A.header,cookies=L);H=I.loads(O.text);C[Br]=0
		if H[M]==0:
			C[Br]=1;C[At]=H[E][V];C[A7]=H[E][A7];C[A8]=H[E][A8];C[A4]=J;C[Bs]=F(H[E]['vipStatus'])
			if D==h:A.session_master.cookies=L;A.userid=C[At];A.csrf=J['bili_jct']
			if C[Bs]:A.session_vip.cookies=L
		else:A.userid=B
		K[D]=C
		with A.con:
			if W(C)>1:A.userConfig.update({c:K})
			if D==h:A.getCookie_event.set()
	getFakeCookie_event=j.Event()
	def getFakeCookie(A,fromSearch=AU):
		if A.session_fake.cookies:A.getFakeCookie_event.set()
		C={};C[A9]=A.header[A9];B=A.fetch(Bt,headers=C);A.session_fake.cookies=B.cookies;A.getFakeCookie_event.set()
		with A.con:D=A.userConfig.get(c,{});D[O]={A4:A2(B.cookies)};A.userConfig.update({c:D})
		if not fromSearch:
			A.getCookie_event.wait()
			if not A.session_master.cookies:A.session_master.cookies=B.cookies
	def get_fav_list_dict(E,fav):A={D:fav[R].replace(k,B).replace(l,B).replace(AJ,AK).strip(),C:fav[m]};return A
	add_fav_filter_event=j.Event()
	def add_fav_filter(B):
		N=B.userConfig.get(c,{})
		if N.get(h)and N[h].get(At):F=B.userConfig[c][h][At]
		else:B.getCookie_event.wait();F=B.userid
		J=[]
		if F:
			P='https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid=%s&jsonp=jsonp'%A(F);Q=B._get_sth(P);L=I.loads(Q.text)
			if L[M]==0 and L.get(E):R=L[E].get(H);J=s(g(B.get_fav_list_dict,R))
		U=[{D:'追番',C:T},{D:'追剧',C:A0}];O=B.config[Z].get(Ad)
		if O:O.insert(0,{S:Ae,K:BK,G:U+J})
		B.add_fav_filter_event.set();B.userConfig[CU]=J
	def get_channel_list_dict(F,channel):A=channel;E={D:A[K].replace(k,B).replace(l,B).replace(AJ,AK).strip(),C:A[m]};return E
	def get_channel_list(A):
		C='https://api.bilibili.com/x/web-interface/web/channel/category/channel/list?id=100&offset=0&page_size=15';D=A._get_sth(C,O);B=I.loads(D.text);G=[]
		if B[M]==0:F=B[E].get('channels');A.userConfig[Au]=s(g(A.get_channel_list_dict,F))
		return A.userConfig[Au]
	add_channel_filter_event=j.Event()
	def add_channel_filter(A):
		C=A.userConfig.get(Au,B);E=A.pool.submit(A.get_channel_list)
		if not C:C=E.result()
		D=A.config[Z].get(Ar,[])
		if D:D.insert(0,{S:n,K:BK,G:C})
		A.config[Z][Ar]=D;A.add_channel_filter_event.set()
	add_focus_on_up_filter_event=j.Event()
	def add_focus_on_up_filter(B):
		N='上个视频的UP主';O=[{D:N,C:N}];F=[]
		if not B.session_master.cookies:B.getCookie_event.wait()
		if B.session_master.cookies:
			P='https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/all?timezone_offset=-480&type=video&page=1';Q=B._get_sth(P);H=I.loads(Q.text)
			if H[M]==0 and H.get(E):R=H[E].get(BL,[]);F=s(g(lambda x:{D:x[BM][Bu][K],C:A(x[BM][Bu][V])},R))
		if W(B.focus_on_up_list)>0:
			T=s(g(lambda x:x[C],B.focus_on_up_list))
			for L in F:
				if L[C]in T:F.remove(L)
			F.extend(B.focus_on_up_list)
		U=[{D:'登录与设置',C:'登录'}];F=O+F+U;J=B.config[Z].get(AI,[])
		if J:J.insert(0,{S:V,K:BN,G:F})
		B.config[Z][AI]=J;B.add_focus_on_up_filter_event.set()
	def get_live_parent_area_list(N,parent_area):B=parent_area;E=B[K];id=A(B[m]);F=B[H];I=s(g(lambda area:{D:area[K],C:A(area['parent_id'])+J+A(area[m])},F));L={S:A1,K:E,G:I};M={m:id+'_0',G:L};return E,M
	def get_live_list(A):
		C='https://api.live.bilibili.com/xlive/web-interface/v1/index/getWebAreaList?source_id=2';D=A._get_sth(C,O);B=I.loads(D.text);G={}
		if B[M]==0:F=B[E][E];A.userConfig[AT]=A2(A.pool.map(A.get_live_parent_area_list,F))
		return A.userConfig[AT]
	def set_default_cateManualLive(A):
		B=[{D:AR,C:AR}]
		for E in A.userConfig[AT]:F={D:E,C:A.userConfig[AT][E][m]};B.append(F)
		A.defaultConfig[y]=B;return B
	add_live_filter_event=j.Event()
	def add_live_filter(A):
		C=A.userConfig.get(AT,{});E=A.pool.submit(A.get_live_list)
		if not C:C=E.result()
		H=A.pool.submit(A.set_default_cateManualLive);A.config[Z][AH]=[];B=A.userConfig.get(y,[])
		if not B:B=H.result()
		if B:I={S:A1,K:BK,G:B};A.config[Z][AH].append(I)
		if F(A.userConfig[Bo]):
			for D in C.values():
				if W(D[G][G])==1:continue
				A.config[Z][AH].append(D[G])
		A.add_live_filter_event.set()
	add_search_key_event=j.Event()
	def add_search_key(A):
		B=A.focus_on_search_key;L='https://api.bilibili.com/x/web-interface/search/square?limit=10&platform=web';N=A._get_sth(L,O);F=I.loads(N.text);Q={}
		if F[M]==0:P=F[E]['trending'].get(H,[]);B+=s(g(lambda x:x[Av],P))
		J={S:Av,K:'搜索词',G:[]};J[G]=s(g(lambda i:{D:i,C:i},B));A.config[Z][BI].insert(0,J);A.add_search_key_event.set()
	def get_tuijian_filter(E):
		J={'番剧时间表':'10001','国创时间表':'10004',Bp:L,'动画':T,'音乐':AQ,'舞蹈':'129','游戏':AV,'鬼畜':'119','知识':'36','科技':'188','运动':'234','生活':'160','美食':'211','动物':'217','汽车':'223','时尚':'155','娱乐':'5',Ac:'181','原创':'origin','新人':'rookie'};M=[{D:BE,C:BK},{D:BF,C:Bp}];F=[]
		for H in M:
			I={S:A1,K:H[C],G:[]};N=E.userConfig.get(H[D],[])
			for A in N:
				B=J.get(A)
				if not B:B=A
				O={D:A,C:B};I[G].append(O)
			F.append(I)
		E.config[Z][AR]=F
	def __init__(A):A.load_config();A.pool.submit(A.getCookie);A.pool.submit(A.getFakeCookie);A.pool.submit(A.getCookie,AS)
	def init(A,extend=B):print('============{0}============'.format(extend))
	def isVideoFormat(A,url):0
	def manualVideoCheck(A):0
	def format_img(B,img):
		A=img;A+='@672w_378h_1c.webp'
		if not A.startswith('http'):A='https:'+A
		return A
	def pagination(A,array,pg):B=A.userConfig[Y]*F(pg);C=B-A.userConfig[Y];return array[C:B]
	def zh(D,num):
		C=num
		if F(C)>=100000000:B=Bj(BC(C)/BC(100000000),1);B=A(B)+'亿'
		elif F(C)>=10000:B=Bj(BC(C)/BC(10000),1);B=A(B)+'万'
		else:B=A(C)
		return B
	def second_to_time(D,a):
		a=F(a)
		if a<3600:C=x.strftime('%M:%S',x.gmtime(a))
		else:C=x.strftime('%H:%M:%S',x.gmtime(a))
		if A(C).startswith(L):C=A(C).replace(L,B,1)
		return C
	def str2sec(E,x):
		x=A(x)
		try:D,B,C=x.strip().split(':');return F(D)*3600+F(B)*60+F(C)
		except:B,C=x.strip().split(':');return F(B)*60+F(C)
	def filter_duration(B,vodlist,key):
		D=vodlist;C=key
		if C==L:return D
		else:E=[D for D in D if B.time_diff1[C][0]<=B.str2sec(A(D[X]))<B.time_diff1[C][1]];return E
	def find_bangumi_id(C,url):
		B=A(url).strip().split(AA)[-1]
		if not B:B=A(url).strip().split(AA)[-2]
		B=B.split('?')[0];return B
	def test_mirror_site(A):
		B=['http://jm92swf.s1002.xrea.com','http://above-mentioned-ice.000webhostapp.com'];C=9;D=B[0]
		for E in B:
			try:G=Bh(E+CV,timeout=2)
			except:continue
			F=G.elapsed.total_seconds()
			if F<C:C=F;D=E
		A.mirror_site=D;A.pool.submit(A._checkUpdate,L)
	def get_Login_qrcode(D,pg):
		R='setting_login_';N='https://www.bilibili.com/favicon.ico';A={}
		if F(pg)!=1:return A
		G=[{Q:'setting_tab&filter',P:'标签与筛选',U:N},{Q:'setting_liveExtra',P:CW,U:N}];J='https://passport.bilibili.com/x/passport-login/web/qrcode/generate';S=D._get_sth(J,O);K=I.loads(S.text)
		if K[M]==0:
			id=K[E]['qrcode_key'];J=K[E][o];T={h:'主账号',AS:'副账号'};V={0:'未登录',1:'已登录'};W={0:B,1:'👑'};Y=D.userConfig.get(c,{})
			for(Z,a)in T.items():
				C=Y.get(Z)
				if C:G.append({Q:R+id,P:C[A8],U:D.format_img(C[A7]),X:W[C[Bs]]+a+AL+V[C[Br]]})
			L={'qrcode':J}
			if not AF.startswith('/data/'):L['qr_chs']='208x117'
			G.append({Q:R+id,P:'有效期3分钟，确认后点这里',U:D.mirror_site+'/?'+CL(L)})
		A[H]=G;A[i]=1;A[t]=1;A[u]=1;A[p]=1;return A
	time_diff1={T:[0,300],A0:[300,900],AQ:[900,1800],AV:[1800,3600],'5':[3600,0x4ee2d6d415b85acef80ffffffff]};time_diff=L;dynamic_offset=B
	def get_dynamic(C,pg,mid,order):
		if mid==L:
			D={}
			if F(pg)==1:C.dynamic_offset=B
			S='https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/all?timezone_offset=-480&type=video&offset=%s&page=%s'%(C.dynamic_offset,pg);T=C._get_sth(S);J=I.loads(T.text)
			if J[M]==0:
				C.dynamic_offset=J[E].get(CX);O=[];V=J[E][BL]
				for N in V:
					if not N['visible']:continue
					W=N[BM][Bu][K];G=N[BM]['module_dynamic']['major'][BO];Y=A(G[a]).strip();Z=G[R].strip().replace(k,B).replace(l,B);b=G[d].strip();c=A(C.second_to_time(C.str2sec(G['duration_text']))).strip()+Aw+A(W).strip();O.append({Q:v+Y,P:Z,U:C.format_img(b),X:c})
				D[H]=O;D[i]=pg;D[t]=9999;D[u]=99;D[p]=999999
			return D
		else:return C.get_up_videos(mid=mid,pg=pg,order=order)
	def get_found_vod(D,vod):
		C=vod;E=C.get(a,B)
		if not E:E=C.get(m,B)
		F=C.get('goto',B)
		if not F or F and F==v:E=v+A(E).strip()
		elif F=='ad':return[]
		M=C[R].strip();N=C[Ax].strip();O=C.get('is_followed')
		if F==AW:
			J=C['room_info'];H=B;S=J.get(CY,B)
			if S:H='直播中  '
			else:return[]
			H+='👁'+J[CZ][Ca]+Aw+C[Af][K].strip()
		else:
			I=C.get('rcmd_reason',B)
			if I and type(I)==A2 and I.get(BP):
				G='  🔥'+I[BP].strip()
				if'人气飙升'in G:G='  🔥人气飙升'
			elif O:G='  已关注'
			else:G=BQ+D.zh(C[Ay][Az])
			H=A(D.second_to_time(C[e])).strip()+BR+D.zh(C[Ay][A_])+G
		L=[{Q:E,P:M,U:D.format_img(N),X:H}]
		for T in D.pool.map(D.get_found_vod,C.get('others',[])):L.extend(T)
		return L
	def get_found(B,tid,rid,pg):
		J=tid;D=pg;F={}
		if J==AR:P=B.encrypt_wbi(fresh_type=4,feed_version='V8',fresh_idx=D,fresh_idx_1h=D,brush=D,homepage_ver=1,ps=B.userConfig[Y]);C=f"https://api.bilibili.com/x/web-interface/wbi/index/top/feed/rcmd?{P}";L=B._get_sth(C)
		else:
			C='https://api.bilibili.com/x/web-interface/ranking/v2?rid={0}&type={1}'.format(rid,J)
			if J==A3:C='https://api.bilibili.com/x/web-interface/popular?pn={0}&ps={1}'.format(D,B.userConfig[Y])
			elif J=='入站必刷':C='https://api.bilibili.com/x/web-interface/popular/precious'
			elif J=='每周必看':C='https://api.bilibili.com/x/web-interface/popular/series/list';L=B._get_sth(C,O);K=I.loads(L.text);Q=K[E][H][0]['number'];C='https://api.bilibili.com/x/web-interface/popular/series/one?number='+A(Q)
			L=B._get_sth(C,O)
		K=I.loads(L.text)
		if K[M]==0:
			N=[];G=K[E].get('item')
			if not G:G=K[E][H]
			if W(G)>B.userConfig[Y]:G=B.pagination(G,D)
			for R in B.pool.map(B.get_found_vod,G):N.extend(R)
			F[H]=N;F[i]=D;F[t]=9999;F[u]=99;F[p]=999999
		return F
	def get_bangumi(D,tid,pg,order,season_status):
		a='first_ep';Z='first_ep_info';V=order;G=tid;J={}
		if V=='追番剧':K='https://api.bilibili.com/x/space/bangumi/follow/list?type={0}&vmid={1}&pn={2}&ps={3}'.format(G,D.userid,pg,D.userConfig[Y]);b=D._get_sth(K)
		else:
			K='https://api.bilibili.com/pgc/season/index/result?type=1&season_type={0}&page={1}&order={2}&season_status={3}&pagesize={4}'.format(G,pg,V,season_status,D.userConfig[Y])
			if V==A3:
				if G==T:K='https://api.bilibili.com/pgc/web/rank/list?season_type={0}&day=3'.format(G)
				else:K='https://api.bilibili.com/pgc/season/rank/web/list?season_type={0}&day=3'.format(G)
			b=D._get_sth(K,O)
		S=I.loads(b.text)
		if S[M]==0:
			if E in S:L=S[E][H]
			else:L=S[AM][H]
			if W(L)>D.userConfig[Y]:L=D.pagination(L,pg)
			c=[]
			for C in L:
				f=A(C[AX]).strip();g=C[R];N=C.get('ss_horizontal_cover')
				if not N or G==T and not D.userConfig[CQ]:
					if C.get(Z)and d in C[Z]:N=C[Z][d]
					elif C.get(a)and d in C[a]:N=C[a][d]
					else:N=C[d].strip()
				F=C.get(B0,B)
				if not F and C.get(B1)and C[B1].get(B0):F=C[B1][B0]
				F=F.replace('更新至','🆕');e=C.get(Ay)
				if e:F='▶'+D.zh(e.get(A_))+'  '+F
				c.append({Q:q+f,P:g,U:D.format_img(N),X:F})
			J[H]=c;J[i]=pg;J[t]=9999;J[u]=90;J[p]=999999
		return J
	def get_timeline(E,tid,pg):
		Z='pub_index';D={};a='https://api.bilibili.com/pgc/web/timeline/v2?season_type={0}&day_before=2&day_after=4'.format(tid);b=E._get_sth(a,O);c=b.text;F=I.loads(c)
		if F[M]==0:
			T=[];G=F[AM]['latest']
			for C in G:J=A(C[AX]).strip();K=C[R].strip();N=C[d].strip();S='🆕'+C[Z]+'  ❤ '+C['follows'].replace('系列',B).replace('追番',B);T.append({Q:q+J,P:K,U:E.format_img(N),X:S})
			V=[];Y=F[AM]['timeline']
			for e in range(W(Y)):
				G=Y[e][BS]
				for C in G:
					if A(C['published'])==L:J=A(C[AX]).strip();K=A(C[R]).strip();N=A(C[d]).strip();f=A(x.strftime('%m-%d %H:%M',x.localtime(C['pub_ts'])));S=f+'   '+C[Z];V.append({Q:q+J,P:K,U:E.format_img(N),X:S})
			D[H]=V+T;D[i]=1;D[t]=1;D[u]=90;D[p]=999999
		return D
	def get_live(G,pg,parent_area_id,area_id):
		V='recommend_room_list';K=parent_area_id;D={}
		if K==AR:J='https://api.live.bilibili.com/xlive/web-interface/v1/webMain/getList?platform=web&page=%s'%pg;N=G._get_sth(J)
		else:
			J='https://api.live.bilibili.com/xlive/web-interface/v1/second/getList?platform=web&parent_area_id=%s&area_id=%s&sort_type=online&page=%s'%(K,area_id,pg)
			if K==A3:J='https://api.live.bilibili.com/room/v1/room/get_user_recommend?page=%s&page_size=%s'%(pg,G.userConfig[Y])
			N=G._get_sth(J,O)
		S=I.loads(N.text)
		if S[M]==0:
			T=[];C=S[E]
			if V in C:C=C[V]
			elif H in C:C=C[H]
			for F in C:
				W=A(F[Cb]).strip();Z=F[R].replace(k,B).replace(l,B).replace(AJ,AK);L=F.get(Cc)
				if not L:L=F.get(d)
				a='👁'+F[CZ][Ca].strip()+Aw+F[A8].strip();T.append({Q:W,P:Z,U:G.format_img(L),X:a})
			D[H]=T;D[i]=pg;D[t]=9999;D[u]=99;D[p]=999999
		return D
	get_up_videos_result={}
	def get_up_videos(C,mid,pg,order):
		S=order;L=pg;D=mid;G={}
		if not D.isdigit():
			if F(L)==1:
				C.get_up_videos_mid=D=C.detailContent_args.get(V,B)
				if not D in C.get_up_videos_result:C.get_up_videos_result.clear();C.get_up_videos_result[D]=[]
			else:D=C.get_up_videos_mid
		if F(L)==1:C.get_up_info_event.clear();C.pool.submit(C.get_up_info,D)
		T=W=B
		if S==Cd:W=S;S=Ag
		elif S==Ce:
			T='投稿: ';J=C.get_up_videos_result.get(D,[])
			if J:G[H]=J;return G
		Z=L
		if W:C.get_up_info_event.wait();Z=C.up_info[D][Bv]-F(L)+1
		e=C.encrypt_wbi(mid=D,pn=Z,ps=C.userConfig[Y],order=S);f=f"https://api.bilibili.com/x/space/wbi/arc/search?{e}";g=C._get_sth(f,O);h=g.text;b=I.loads(h);J=[]
		if b[M]==0:
			j=b[E][H]['vlist']
			for N in j:
				m=A(N[a]).strip();n=N[R].strip().replace(k,B).replace(l,B);o=N[Ax].strip();c=C.second_to_time(C.str2sec(A(N['length']).strip()))+BR+C.zh(N[Bw])
				if not T:c+=BQ+C.zh(N['video_review'])
				J.append({Q:v+m,P:T+n,U:C.format_img(o),X:c})
			if W:J.reverse()
			if F(L)==1:
				C.get_up_info_event.wait();d=C.up_info[D][K]+Cf
				if T:d='UP: '+C.up_info[D][K]
				q={Q:AY+A(D),P:d,U:C.format_img(C.up_info[D][A7]),X:C.up_info[D][Ah]+'  👥'+C.up_info[D][Ai]+'  🎬'+A(C.up_info[D][BT])};J.insert(0,q)
			if T:C.get_up_videos_result[D]=J
			G[H]=J;G[i]=L;G[t]=99;G[u]=99;G[p]=999999
		return G
	history_view_at=0
	def get_history(D,type,pg):
		W='progress';G={}
		if F(pg)==1:D.history_view_at=0
		Z='https://api.bilibili.com/x/web-interface/history/cursor?ps={0}&view_at={1}&type={2}'.format(D.userConfig[Y],D.history_view_at,type)
		if type==BU:Z='https://api.bilibili.com/x/v2/history/toview'
		f=D._get_sth(Z);T=I.loads(f.text)
		if T[M]==0:
			b=[];V=T[E].get(H,[])
			if type==BU:V=D.pagination(V,pg)
			else:D.history_view_at=T[E]['cursor']['view_at']
			for C in V:
				J=C.get('history',B)
				if J:K=J['business'];N=A(J['oid']).strip();c=C[d].strip();S=A(J[Bx]).strip()
				else:K=BO;N=A(C[a]).strip();c=C[Ax].strip();S=A(C[i][Bx]).strip()
				if K=='article':continue
				elif K=='pgc':N=z+A(J['epid']);e=C[p];S=C.get('show_title')
				elif K==BO:N=v+N;e=C[Cg]
				g=C[R].replace(k,B).replace(l,B).replace(AJ,AK)
				if K==AW:h=C.get('badge',B);O=h+Aw+C['author_name'].strip()
				else:
					if A(C[W])=='-1':O='已看完'
					elif A(C[W])==L:O='刚开始看'
					else:j=A(D.second_to_time(C[W])).strip();O='看到  '+j
					if not e in[0,1]and S:O+=' ('+A(S)+')'
				b.append({Q:N,P:g,U:D.format_img(c),X:O})
			G[H]=b;G[i]=pg;G[t]=9999;G[u]=90;G[p]=999999
		return G
	def get_fav_detail(F,pg,mlid,order):
		K='cnt_info';D={};L='https://api.bilibili.com/x/v3/fav/resource/list?media_id=%s&order=%s&pn=%s&ps=10&platform=web&type=0'%(mlid,order,pg);N=F._get_sth(L);O=N.text;G=I.loads(O)
		if G[M]==0:
			J=[];S=G[E]['medias']
			for C in S:
				if C.get(r)in[2]and C.get(R)!='已失效视频':T=A(C[m]).strip();V=C[R].replace(k,B).replace(l,B).replace(AJ,AK);W=C[d].strip();Y=A(F.second_to_time(C[e])).strip()+BR+F.zh(C[K][Bw])+Ch+F.zh(C[K][Az]);J.append({Q:v+T+'_mlid'+A(mlid),P:V,U:F.format_img(W),X:Y})
			D[H]=J;D[i]=pg;D[t]=9999;D[u]=99;D[p]=999999
		return D
	get_up_info_event=j.Event();up_info={}
	def get_up_info(D,mid,**P):
		O='Official';J=mid
		if J in D.up_info:D.get_up_info_event.set()
		G=P.get(E)
		if not G:
			Q='https://api.bilibili.com/x/web-interface/card?mid={0}'.format(J);S=D._get_sth(Q);L=I.loads(S.text)
			if L[M]==0:G=L[E]
			else:D.get_up_info_event.set();return
		H=G['card'];C={};C[Ah]='未关注'
		if G[Ah]:C[Ah]='已关注'
		C[K]=H[K].replace(k,B).replace(l,B);C[A7]=H[A7];C[Ai]=D.zh(H[Ai]);C[By]=D.zh(G[By]);C[BT]=A(G['archive_count']).strip();C[AZ]=H[O][AZ]+Aa+H[O][R];N=divmod(F(C[BT]),D.userConfig[Y]);C[Bv]=N[0]
		if N[1]!=0:C[Bv]+=1
		D.up_info[J]=C;D.get_up_info_event.set()
	def get_vod_relation(H,id):
		if id.isdigit():F='aid='+A(id)
		elif'='in id:F=id
		else:F='bvid='+id
		J='https://api.bilibili.com/x/web-interface/archive/relation?'+F;K=H._get_sth(J);B=I.loads(K.text);C=[]
		if B[M]==0:
			B=B[E]
			if B[Ci]:C.append('已关注')
			else:C.append('未关注')
			D=[]
			if B[Cj]:D.append('⭐')
			if B[B2]:D.append('👍')
			G=B.get(Bz)
			if G:D.append('💰'*G)
			if W(D)==3:C.append('👍💰⭐')
			else:C.extend(D)
			if B['dislike']:C.append('👎')
			if B['season_fav']:C.append('已订阅合集')
		return C
	def get_channel(C,pg,cid,order):
		R=order;N='uri';F={}
		if A(pg)==T:C.channel_offset=B
		if R==Ck:S='https://api.bilibili.com/x/web-interface/web/channel/featured/list?channel_id={0}&filter_type=0&offset={1}&page_size={2}'.format(cid,C.channel_offset,C.userConfig[Y])
		else:S='https://api.bilibili.com/x/web-interface/web/channel/multiple/list?channel_id={0}&sort_type={1}&offset={2}&page_size={3}'.format(cid,R,C.channel_offset,C.userConfig[Y])
		f=C._get_sth(S,O);L=I.loads(f.text)
		if L.get(M)==0:
			C.channel_offset=L[E].get(CX);V=[];G=L[E][H]
			if pg==T and BL in G[0]:g=G[0][BL];del G[0];G=g+G
			for D in G:
				if N in D and B_ in D[N]:W=C.find_bangumi_id(D[N])
				else:W=v+A(D[m]).strip()
				h=D[K].replace(k,B).replace(l,B).replace(AJ,AK);j=D[d].strip();J='▶'+A(D['view_count']);Z=D.get(e,B)
				if Z:J=A(C.second_to_time(C.str2sec(Z))).strip()+'  '+J
				a=D.get(Az,B);b=D.get('like_count',B);c=D.get('follow_count',B)
				if a:J+=BQ+C.zh(a)
				elif b:J+='  👍'+A(b)
				elif c:J+='  ❤'+A(c)
				V.append({Q:W,P:h,U:C.format_img(j),X:J})
			F[H]=V;F[i]=pg;F[t]=9999;F[u]=99;F[p]=999999
		return F
	def get_follow(G,pg,sort):
		J=pg;D=sort;L={}
		if D=='最常访问':N='https://api.bilibili.com/x/relation/followings?vmid={0}&pn={1}&ps=10&order=desc&order_type=attention'.format(G.userid,J)
		elif D==C0:N='https://api.bilibili.com/x/relation/followings?vmid={0}&pn={1}&ps=10&order=desc&order_type='.format(G.userid,J)
		elif D==B3:N='https://api.live.bilibili.com/xlive/web-ucenter/v1/xfetter/GetWebList?page={0}&page_size=10'.format(J)
		elif D==BV:N='https://api.bilibili.com/x/v2/history?pn={0}&ps=15'.format(J)
		elif D==B4:N='https://api.bilibili.com/x/relation/tag?mid={0}&tagid=-10&pn={1}&ps=10'.format(G.userid,J)
		elif D==C1:N='https://api.bilibili.com/x/relation/whispers?pn={0}&ps=10'.format(J)
		else:N='https://api.bilibili.com/x/relation/followers?vmid={0}&pn={1}&ps=10&order=desc&order_type=attention'.format(G.userid,J)
		b=G._get_sth(N);S=I.loads(b.text)
		if S[M]!=0:return L
		if D==B4 or D==BV:T=S[E]
		elif D==B3:T=S[E]['rooms']
		else:T=S[E][H]
		if F(J)==1:G.recently_up_list=[]
		a=[]
		for C in T:
			W=B
			if D==BV:
				O=AY+A(C[Af][V])
				if O in G.recently_up_list:continue
				G.recently_up_list.append(O);Y=A(C[Af][K]).strip();Z=A(C[Af][A7]).strip()
			elif D==B3:O=A(C[Cl]);Y=C[R].replace(k,B).replace(l,B).replace(AJ,AK);Z=C['cover_from_user'].strip();W=C[A8].strip()
			else:O=AY+A(C[V]);Y=A(C[A8]).strip();Z=A(C[A7]).strip()
			if C2 in C and C[C2]==1:W=B4
			a.append({Q:O,P:Y,U:G.format_img(Z),X:W})
		L[H]=a;L[i]=J;L[t]=9999;L[u]=99;L[p]=999999;return L
	homeVideoContent_result={}
	def homeVideoContent(A):
		if not A.homeVideoContent_result:B=A.get_found(rid=L,tid=C3,pg=1)[H][0:F(A.userConfig[Bl])];A.homeVideoContent_result[H]=B
		return A.homeVideoContent_result
	def categoryContent(H,tid,pg,filter,extend):
		K=pg;E=tid;D=extend;H.stop_heartbeat_event.set()
		if E==AR:
			if A1 in D:E=D[A1]
			if E.isdigit():
				E=F(E)
				if E>10000:E-=10000;return H.get_timeline(tid=E,pg=K)
				R=E;E=C3;return H.get_found(tid=E,rid=R,pg=K)
			R=L;return H.get_found(tid=E,rid=R,pg=K)
		elif E==Ac:
			E=T;I=A3;U='-1'
			if A1 in D:E=D[A1]
			if b in D:I=D[b]
			if C4 in D:
				if I==A3:I=A0
				U=D[C4]
			return H.get_bangumi(E,K,I,U)
		elif E==AI:
			M=L;I=Ag
			if V in D:M=D[V]
			if b in D:I=D[b]
			if M==L and not H.userid or M=='登录':return H.get_Login_qrcode(K)
			return H.get_dynamic(pg=K,mid=M,order=I)
		elif E==Ar:
			I='hot';P=random.choice(H.userConfig[Au]);P=P[C]
			if b in D:I=D[b]
			if n in D:P=D[n]
			return H.get_channel(pg=K,cid=P,order=I)
		elif E==AH:
			E=A3;X=L
			if A1 in D:E=D[A1]
			if J in E:a=E.split(J);E=a[0];X=a[1]
			return H.get_live(pg=K,parent_area_id=E,area_id=X)
		elif E==A6:
			M=H.detailContent_args.get(V,B)
			if V in D:M=D[V]
			if not M or M=='登录':return H.get_Login_qrcode(K)
			c=H.config[Z].get(A6)
			if not M and c:
				for N in c:
					if N[S]==V:
						if W(N[G])>1:M=N[G][1][C]
						break
			I=Ag
			if b in D:I=D[b]
			return H.get_up_videos(mid=M,pg=K,order=I)
		elif E==BG:
			d='最常访问'
			if C5 in D:d=D[C5]
			return H.get_follow(K,d)
		elif E==Ad:
			O=A(H.userConfig[Bm])
			if Ae in D:O=D[Ae]
			f=H.config[Z].get(Ad)
			if O in[T,A0]:return H.get_bangumi(tid=O,pg=K,order='追番剧',season_status=B)
			elif O==L and f:
				for N in f:
					if N[S]==Ae:
						if W(N[G])>1:O=N[G][2][C]
						break
			I='mtime'
			if b in D:I=D[b]
			return H.get_fav_detail(pg=K,mlid=O,order=I)
		elif E==BH:
			type=C3
			if r in D:type=D[r]
			if type==BN:return H.get_follow(pg=K,sort=BV)
			return H.get_history(type=type,pg=K)
		else:
			g=L
			if e in D:g=D[e]
			type=AB
			if r in D:type=D[r]
			I=Cm
			if b in D:I=D[b]
			Q=A(H.search_key);h=H.config[Z].get(BI)
			if not Q and h:
				for N in h:
					if N[S]==Av:
						if W(N[G])>0:Q=N[G][0][C]
						break
			if Av in D:Q=D[Av]
			return H.get_search_content(key=Q,pg=K,duration_diff=g,order=I,type=type,ps=H.userConfig[Y])
	def get_search_content(D,key,pg,duration_diff,order,type,ps):
		K=pg;S=AU
		if not K.isdigit():S=K;K=1
		b=D.encrypt_wbi(keyword=key,page=K,duration=duration_diff,order=order,search_type=type,page_size=ps);c=f"https://api.bilibili.com/x/web-interface/wbi/search/type?{b}";f=D._get_sth(c,O);g=f.text;W=I.loads(g);F={}
		if W.get(M)==0 and AM in W[E]:
			Y=[];L=W[E].get(AM)
			if L and type==AW:L=L.get('live_room')
			if not L:return F
			for C in L:
				J=B
				if type==C6:G=AY+A(C[V]).strip();T=C['upic'].strip();N='👥'+D.zh(C[Ai])+'  🎬'+D.zh(C[Cg]);J=C[A8]
				elif type==AW:G=A(C[Cb]).strip();T=C[d].strip();N='👁'+D.zh(C['online'])+Aw+C[A8]
				elif'media'in type:
					G=A(C[AX]).strip()
					if D.detailContent_args:
						h=D.detailContent_args.get(B5)
						if h:
							Z=[]
							for j in D.detailContent_args[B5]:Z.append(j[Q])
							if G+q in Z:continue
					G=q+G;T=C[d].strip();N=A(C[B0]).strip().replace('更新至','🆕')
				else:
					G=v+A(C[a]).strip();T=C[Ax].strip();N=A(D.second_to_time(D.str2sec(C[e]))).strip()+BR+D.zh(C[Bw])
					if S==AU:N+=BQ+D.zh(C[Az])
				if not J:J=C[R].replace(k,B).replace(l,B).replace(AJ,AK).replace('&amp;','&')
				if S:J=S+J
				Y.append({Q:G,P:J,U:D.format_img(T),X:N})
			F[H]=Y;F[i]=K;F[t]=9999;F[u]=99;F[p]=999999
		return F
	def cleanSpace(A,str):return str.replace('\n',B).replace('\t',B).replace('\r',B).replace(AL,B)
	def get_normal_episodes(C,episode):
		G=episode;L=H=B;M=G.get(a,B)
		if not M:M=C.detailContent_args[a]
		U=G.get(n,B);K=G.get(R,B)
		if not K:K=G.get(Bx,B)
		E=G.get(e,B)
		if not E:
			V=G.get(i,B)
			if V:E=V[e]
		D=I=W=Q=B;L=C.detailContent_args.get(B6,B)
		if L:
			L='_ss'+L;H=G.get(m,B)
			if H:H='_ep'+A(H)
			if E and A(E).endswith(C7):E=F(E/1000)
			if K.isdigit():K='第'+K+C.detailContent_args[C8]
			D=G.get('badge',B)
			if not C.session_vip.cookies and D=='会员'and C.userConfig[CR]or D=='付费'and C.userConfig[CS]:Q='_parse'
			if C.session_vip.cookies and C.userConfig[CP]:D=D.replace('会员',B)
			if C.userConfig[CO]and D=='预告':D=D.replace('预告',B);W=1
			if D:D='【'+D+'】'
			I=G.get('long_title',B)
			if not D and I:I=AL+I
		S=K+D+I;S=S.replace(N,AC).replace(w,AD)
		if E:E='_dur'+A(E)
		O='{0}${1}_{2}{3}{4}{5}'.format(S,M,U,L,H,E);P=C.detailContent_args.get(B7,B)
		if J+A(P)==H:C.detailContent_args[B7]=O
		X=C.detailContent_args.get(Aj)
		if J+A(P)==H or not P and X==AU:
			C.detailContent_args[Aj]=B
			if C.userConfig[Ap]:C.get_vod_hot_reply_event.clear();C.pool.submit(C.get_vod_hot_reply,M)
		if L:
			if W:return O,B
			if Q:
				C.detailContent_args[Ak]=1
				if I:I='【解析】'+I
				K+=I;T='{0}${1}_{2}{3}{4}{5}{6}'.format(K,M,U,L,H,E,Q)
				if J+A(P)==H:C.detailContent_args[B7]+=N+T
			else:T=O
			return O,T
		else:return O
	def get_ugc_season(B,section,sections_len):
		C=section
		if sections_len>1:A=B.detailContent_args[Al]+AL+C[R]
		else:A=B.detailContent_args[Al]
		A=A.replace(N,AC).replace(w,AD);D=C.get(BS);E=N.join(g(B.get_normal_episodes,D));F=A,E;return F
	get_vod_hot_reply_event=j.Event()
	def get_vod_hot_reply(G,oid):
		b='member';c='http://api.bilibili.com/x/v2/reply/main?type=1&ps=30&oid='+A(oid);d=G._get_sth(c,O);L=I.loads(d.text)
		if L[M]==0:
			H=L[E].get('replies');Y=L[E].get('top_replies')
			if H and Y:H=Y+H
			if H:
				e=L[E]['upper'][V];T=[];U=[]
				for D in H:
					f=D['rpid'];K=D[b]['sex']
					if K and K=='女':K='👧'
					else:K='👦'
					W=K+D[b][A8]+'：';g=D[V]
					if g==e:W='🆙'+W
					h='👍'+G.zh(D[B2]);Z=D[BP][Cn]
					if'/note-app/'in Z:continue
					F=h+AL+W+Z;F=F.replace(N,AC).replace(w,AD);F+=w+A(oid)+J+A(f)+'_notplay_reply';T.append(F);i=D[BP].get('jump_url',{})
					for(C,X)in i.items():
						if not X.get('app_url_schema')and not X.get('pc_url'):
							if C.startswith('https://www.bilibili.com/'):
								C=A(C).split('?')[0].split(AA)
								while C[-1]==B:C.pop(-1)
								C=C[-1]
							if C.startswith(Co)or C.startswith(BW)or C.startswith(z)or C.startswith(q):
								S=A(X[R]).replace(N,AC).replace(w,AD);a={Q:A(C),P:'评论：'+S}
								if not a in U:U.append(a)
								S='快搜：'+A(C)+AL+S;F=S+BX;T.append(F)
				G.detailContent_args[Aj]=N.join(T);G.detailContent_args[Cp]=U
		G.get_vod_hot_reply_event.set()
	detailContent_args={}
	def detailContent(G,array):
		c=array;G.stop_heartbeat_event.set();L=c[0]
		if L.startswith(BY):return G.interaction_detailContent(L)
		G.detailContent_args={}
		if L.startswith(Co):
			try:
				A8=Bh(url=L,headers=G.header,allow_redirects=False);d=A8.headers['Location'].split('?')[0].split(AA)
				while d[-1]==B:d.pop(-1)
				L=d[-1]
				if not L.startswith(BW,0,2):return{}
			except:return{}
		id=t=j=B;G.get_vod_hot_reply_event.set()
		if L.startswith(Cq):
			L=L.split(J)
			if L[1]=='tab&filter':return G.setting_tab_filter_detailContent()
			elif L[1]=='liveExtra':return G.setting_liveExtra_detailContent()
			elif L[1]=='login':A9=L[2];return G.setting_login_detailContent(A9)
		elif L.startswith(v)or L.startswith(BW):
			for T in L.split(J):
				if T.startswith(v):id=T.replace(v,B,1);j='aid='+A(id)
				elif T.startswith(BW):id=T;j='bvid='+id
				elif T.startswith(Ae):t=T.replace(Ae,B,1)
			if G.userConfig[Ap]:G.detailContent_args[Aj]=B;G.get_vod_hot_reply_event.clear();G.pool.submit(G.get_vod_hot_reply,id)
		elif AY in L:return G.up_detailContent(c)
		elif q in L or z in L:return G.ysContent(c)
		elif L.isdigit():return G.live_detailContent(c)
		AB=G.pool.submit(G.get_vod_relation,j);d='https://api.bilibili.com/x/web-interface/view/detail?'+j;AE=G._get_sth(d,O);m=I.loads(AE.text)
		if m[M]!=0:return{}
		S=m[E]['View'];A0=S.get(BZ,B)
		if B_ in A0:
			AF=G.find_bangumi_id(A0);u=[]
			for T in c:u.append(T)
			u[0]=AF;return G.ysContent(u)
		G.detailContent_args[V]=A1=A(S[Af][V]);G.detailContent_args[a]=L=S.get(a);G.pool.submit(G.get_up_info,mid=A1,data=m[E].get('Card'));n=S.get('ugc_season')
		if n:
			G.detailContent_args[Al]=n[R];A2=n['sections'];AG=W(A2);A3=[]
			for AH in A2:o=G.pool.submit(G.get_ugc_season,AH,AG);A3.append(o)
		A4=m[E].get('Related');A5=S['pages'];AI=S[R].replace(k,B).replace(l,B);AJ=S[Ax];AK=S[Af][K];AL=S[AZ].strip();AM=S['tname'];AP=x.strftime('%Y%m%d',x.localtime(S[Ag]));g=S[Ay];Z=[];Z.append('▶'+G.zh(g[A_]));Z.append('💬'+G.zh(g[Az]));Z.append('👍'+G.zh(g[B2]));h=S.get('honor_reply')
		if h:Z.insert(0,'🏅'+h['honor'][0][AZ])
		if not h or h and h['honor'][0][r]==4:Z.append('💰'+G.zh(g[Bz]));Z.append('⭐'+G.zh(g[Cj]))
		AQ=A(S[e]).strip();Ao=S[e];A6=S['rights'].get('is_stein_gate',0);i={Q:v+A(L),P:AI,U:AJ,BJ:AM,C9:AP,CA:Cr,X:AQ,Ba:Aa.join(Z),Ab:AL};y=[]
		if G.userid:
			AR=Cs;AS=Ct;AT='👍点赞$1_notplay_like';AU='👍🏻取消点赞$2_notplay_like';AV='👍💰投币$1_notplay_coin';AW='👍💰💰投2币$2_notplay_coin';AX='👍💰⭐三连$notplay_triple';p=[AR,AX,AT,AV,AW,AS,AU]
			if t:Ac=f"☆取消收藏${t}_del_notplay_fav";p.append(Ac)
			for s in G.userConfig.get(CU,[]):Ad=s[D].replace(N,AC).replace(w,AD);Ah=s[C];s='⭐{}${}_add_notplay_fav'.format(Ad,Ah);p.append(s)
			Ak=F(G.userConfig[An])
			if Ak>116:p.append('⚠️限高1080$116_notplay_vodTMPQn')
			y=[N.join(p)]
		Y=[];b=[]
		if A5:
			Y=['B站']
			if A6:Y=['互动视频【快搜继续】']
			b=[N.join(G.pool.map(G.get_normal_episodes,A5))]
		if y:Y.append('做点什么');b.extend(y)
		if A4:Y.append('相关推荐');b.append(N.join(G.pool.map(G.get_normal_episodes,A4)))
		if G.userConfig[Ap]:
			G.get_vod_hot_reply_event.wait();A7=G.detailContent_args.get(Aj,B)
			if A7:Y.append('热门评论');b.extend([A7])
		if n:
			for o in Bi(A3):Y.append(o.result()[0]);b.append(o.result()[1])
		i[AN]=f.join(Y);i[AO]=f.join(b);i[CB]='🆙 '+AK+Cu+G.up_info[A1][Ai]+Aa+Aa.join(AB.result())
		if A6:G.detailContent_args['AllPt']=Y.copy();G.detailContent_args['AllPu']=b.copy();G.detailContent_args[Cv]=i.copy()
		Am={H:[i]};return Am
	def interaction_detailContent(C,array=B):
		F=array;F=F.split(J);V=G=0
		for D in F:
			if D.startswith(BY):G=D.replace(BY,B)
			elif D.startswith(n):V=D.replace(n,B)
		W=C.detailContent_args.get(a);c=C.detailContent_args.get(B8);K='https://api.bilibili.com/x/stein/edgeinfo_v2?aid={0}&graph_version={1}&edge_id={2}'.format(W,c,G);d=C._get_sth(K,O);e=I.loads(d.text);L=e.get(E);X={}
		if L:
			g=L['edges'].get('questions',[]);M=[]
			for Y in g:
				S=A(Y.get(R,B))
				if S:S+=AL
				for T in Y.get('choices',[]):h=A(T[m]);i=A(T[n]);j=A(T.get('option',B));M.append({Q:BY+h+J+n+i,P:'互动：'+S+j})
			C.detailContent_args[CC]=M.copy()
			if G:
				Z=C.detailContent_args['AllPt'].copy()
				if not M:Z[0]='互动视频'
				b=C.detailContent_args['AllPu'].copy();k=A(L[R]).replace(N,AC).replace(w,AD);K='{0}${1}_{2}'.format(k,W,V);b[0]=K;U=C.detailContent_args[Cv].copy();U[AN]=f.join(Z);U[AO]=f.join(b);X[H]=[U]
		return X
	def up_detailContent(D,array):D.detailContent_args[V]=E=array[0].replace(AY,B);D.get_up_info_event.clear();D.pool.submit(D.get_up_info,E);I=Cw;J='关注$1_notplay_follow';L='取消关注$2_notplay_follow';M='悄悄关注$3_notplay_follow';O='特别关注$-10_notplay_special_follow';R='取消特别关注$0_notplay_special_follow';F=[I,J,M,O,L,R];F=N.join(F);D.get_up_info_event.wait();C=D.up_info[E];G={Q:AY+A(E),P:C[K]+Cf,U:C[A7],X:B,'vod_tags':'mv',Ba:'👥 '+C[Ai]+'\u3000🎬 '+C[BT]+'\u3000👍 '+C[By],CB:'🆙 '+C[K]+Aa+C[Ah]+Cx+A(E),Ab:C[AZ],AN:'关注TA$$$视频投稿在动态标签——筛选——上个UP，选择后查看'};G[AO]=F;S={H:[G]};return S
	def setting_login_detailContent(E,key):
		b='检查失败';M=key;G='f';D='d';C='c';c=E.cookie_dic_tmp.get(M,B);K=B
		if not c:K=E.get_cookies(M)
		if K:K=f"【{K}】通过手机客户端扫码确认登录后点击相应按钮设置账号"
		else:K='【已扫码并确认登录】请点击相应按钮设置当前获取的账号为：'
		R={P:'登录与设置',Ab:'通过手机客户端扫码并确认登录后，点击相应按钮设置cookie，设置后不需要管嗅探结果，直接返回二维码页面刷新，查看是否显示已登录，已登录即可重新打开APP以加载全部标签'};X=['登录$$$退出登录'];O=[];d=K+BX;e='设置为主账号，动态收藏关注等内容源于此$'+A(M)+'_master_login_setting';g='设置为备用的VIP账号，仅用于播放会员番剧$'+A(M)+'_vip_login_setting';O.append(N.join([d,e,g]));h='点击相应按钮退出账号>>>$ ';i='退出主账号$master_logout_setting';j='退出备用的VIP账号$vip_logout_setting';O.append(N.join([h,i,j]));Y=[{G:'主页站点推荐栏',C:Bl,D:{AQ:'3图',AV:'4图','6':'6图','8':'8图','10':'10图'}},{G:'视频画质',C:An,D:E.vod_qn_id},{G:'视频编码',C:Bn,D:E.vod_codec_id},{G:'音频码率',C:Ao,D:E.vod_audio_id},{G:'收藏默认显示',C:Bm,D:{L:'默认收藏夹',T:'追番',A0:'追剧'}},{G:'上传播放进度',C:BD,D:{L:'关','15':'开'}},{G:'直播筛选细化',C:Bo,D:{L:'关',T:'开'}}];S={G:'检查更新',C:CD};U=E.userConfig.get(AP,b);V=Z=0
		if U!=b:U='远端：'+A(E.userConfig[AP][CE]);Z=1;V=E.userConfig[AP].get(Bb)
		S[D]={A(Z):U}
		if V:S[D][AL]=V
		Y.insert(0,S)
		for I in Y:
			X.append(I[G])
			if I[C]==CD:Q=E.userConfig[Bk]
			else:Q=I[D][A(F(E.userConfig[I[C]]))]
			if Ao==I[C]:Q=A(Q).replace(C7,'k')
			a=['当前：'+Q+BX]
			for(id,W)in I[D].items():
				if Ao==I[C]:W=A(W).replace(C7,'k')
				a.append(W+w+A(id)+J+I[C]+'_setting')
			O.append(N.join(a))
		R[AN]=f.join(X);R[AO]=f.join(O);k={H:[R]};return k
	def setting_tab_filter_detailContent(I):
		L={P:'标签与筛选',Ab:'依次点击各标签，同一标签第一次点击为添加，第二次删除，可以返回到二维码页后重进本页查看预览，最后点击保存，未选择的将追加到末尾，如果未保存就重启app，将丢失未保存的配置'};M=[];O=[];U=[{D:Aq,C:'标签'},{D:BE,C:'推荐[分区]'},{D:BF,C:'推荐[排行榜]'},{D:y,C:AH}]
		for Q in U:
			E=Q[D];M.append(Q[C]);F=I.userConfig.get(A(E)+AE,[]);R=B
			if F:R='【未保存】'
			else:F=I.userConfig.get(E,[])
			if not F:F=I.defaultConfig.get(E)
			if F and type(F[0])==A2:F=s(g(lambda x:x[D],F))
			S=['当前: '+','.join(F)+BX,f"{R}点击这里保存$_{E}_save_setting",f"点击这里恢复默认并保存$_{E}_clear_setting"];K=I.defaultConfig[E].copy()
			if E==Aq and not A6 in K:K.append(A6)
			elif E==y:V=I.userConfig.get(A5,[]);K.extend(V.copy())
			for G in K:
				T=A(G)
				if type(G)==A2:T=G[D]+Am+G[C].replace(J,Am);G=G[D]
				S.append(f"{G}${T}_{E}_setting")
			O.append(N.join(S))
		L[AN]=f.join(M);L[AO]=f.join(O);W={H:[L]};return W
	def setting_liveExtra_detailContent(I):
		Q='_liveFilter_setting';F={P:CW,Ab:'点击想要添加的标签，同一标签第一次点击为添加，第二次删除，完成后在[标签与筛选]页继续操作，以添加到直播筛选分区列中'};K=['已添加'];R=I.userConfig.get(A5,[]);E=['点击相应标签(只)可以删除$ #清空$clear_liveFilter_setting']
		for B in R:S=B[C];B=B[D];E.append(B+w+'del_'+B+J+S+Q)
		E=[N.join(E)];T=I.userConfig.get(AT,{})
		for(U,V)in T.items():
			L=V[G][G]
			if W(L)==1:continue
			K.append(U);M=[]
			for O in L:B=A(O[D]).replace(J,'-').replace(N,AC).replace(w,AD);id=A(O[C]).replace(J,Am).replace(N,AC).replace(w,AD);M.append(B+'$add_'+B+J+id+Q)
			E.append(N.join(M))
		F[AN]=f.join(K);F[AO]=f.join(E);X={H:[F]};return X
	def get_all_season(C,season):
		B=season;D=A(B[AX]);E=B[Al]
		if D==C.detailContent_args[B6]:C.detailContent_args[B9]=E
		F=B[d];G=B[B1][B0];H={Q:D+q,P:'系列：'+E,U:C.format_img(F),X:G};return H
	def get_bangumi_section(B,section):
		A=section;C=A[R].replace(N,AC).replace(w,AD);D=A[r]
		if D in[1,2]and W(A['episode_ids'])==0:E=A[BS];F=N.join(g(lambda x:B.get_normal_episodes(x)[0],E));return C,F
	def ysContent(C,array):
		p='rating';E=array[0]
		if z in E:C.detailContent_args[B7]=E;E='ep_id='+E.replace(z,B)
		elif q in E:E='season_id='+E.replace(q,B)
		t='https://api.bilibili.com/pgc/view/web/season?{0}'.format(E);u=C._get_sth(t,O);v=I.loads(u.text);D=v[AM];C.detailContent_args[B6]=A(D[AX]);w=D[R];C.detailContent_args[B9]=D[Al];C.detailContent_args[C8]='集'
		if D[r]in[1,4]:C.detailContent_args[C8]='话'
		M=D.get(B5)
		if W(M)==1:C.detailContent_args[B9]=M[0][Al];M=0
		else:C.detailContent_args[B5]=s(C.pool.map(C.get_all_season,M))
		g=D.get(BS);h=[]
		for K in D.get('section',[]):
			if K:b=C.pool.submit(C.get_bangumi_section,K);h.append(b)
		x=D[d];y=D['share_sub_title'];A0=D['publish']['pub_time'][0:4];A1=D['evaluate'];A2=D[B1][AZ];S=D[Ay];c='▶'+C.zh(S['views'])+Ch+C.zh(S['danmakus'])+'\u3000👍'+C.zh(S['likes'])+'\u3000💰'+C.zh(S['coins'])+'\u3000❤'+C.zh(S['favorites'])
		if p in D:c=A(D[p]['score'])+'分\u3000'+c
		e={Q:q+C.detailContent_args[B6],P:w,U:x,BJ:y,C9:A0,CA:Cr,X:A2,Ba:c,Ab:A1};a=[];G=[]
		if C.userid:
			a=['做点什么'];G='是否追番剧$ #❤追番剧$add_notplay_zhui#💔取消追番剧$del_notplay_zhui';A3=F(C.userConfig[An])
			if A3>116:G+='#⚠️限高1080$116_notplay_vodTMPQn'
			G=[G]
		if M:a.append('更多系列');G.append('更多系列在快速搜索中查看$ #')
		i=[];T=[];j=[];V=[];k=[];L=[]
		if g:
			for(l,m)in C.pool.map(C.get_normal_episodes,g):
				if m:T.append(l);L.append(m)
				else:V.append(l)
			if T:i=[C.detailContent_args[B9]];T=[N.join(T)]
			if V:j=['预告'];V=[N.join(V)]
			if not C.detailContent_args.get(Ak):L=[]
			if L:k=[A(C.detailContent_args[B9])+'【解析】'];L=[N.join(L)]
		Y=k+i+j;Z=L+T+V
		for b in Bi(h):
			K=b.result()
			if K:Y.append(K[0]);Z.append(K[1])
		n=C.detailContent_args.get(B7,B)
		if J in n:Y=['B站']+Y;Z=[n]+Z
		if C.userConfig[Ap]:
			C.get_vod_hot_reply_event.wait();o=C.detailContent_args.get(Aj,B)
			if o:a.append('热门评论');G.append(o)
		Y.insert(1,f.join(a));Z.insert(1,f.join(G));e[AN]=f.join(Y);e[AO]=f.join(Z);A4={H:[e]};return A4
	def get_live_api2_playurl(P,room_id):
		Q=room_id;D='qn';R=[];S=[];H='https://api.live.bilibili.com/xlive/web-room/v2/index/getRoomPlayInfo?room_id={0}&no_playurl=0&mask=1&qn=0&platform=web&protocol=0,1&format=0,1,2&codec=0,1&dolby=5&panorama=1'.format(Q);Z=P._get_sth(H,O);U=I.loads(Z.text)
		if U[M]==0:
			K=U[E].get(Cy,B)
			if K:
				a=K[CF][Cz];C={Bc:{'avc':L,'hevc':T},Bd:{'flv':L,'ts':T,'fmp4':A0}};C[D]=A2(P.pool.map(lambda x:(x[D],x[AZ]),K[CF]['g_qn_desc']));V=[]
				for b in a:V.extend(b[Bd])
				F={}
				for W in V:
					format=A(W.get('format_name'))
					for X in W[Bc]:
						Y=A(X.get('codec_name'));c=X.get('accept_qn')
						for G in c:
							H=format+J+Y+'$liveapi2_'+A(G)+J+C[Bd][format]+J+C[Bc][Y]+J+A(Q)
							if not F.get(C[D][G]):F[C[D][G]]=[]
							F[C[D][G]].append(H)
				for(d,e)in F.items():R.append(d);S.append(N.join(e))
		f={'From':R,o:S};return f
	def live_detailContent(C,array):
		F=array[0];X=C.pool.submit(C.get_live_api2_playurl,F);c='https://api.live.bilibili.com/room/v1/Room/get_info?room_id='+A(F);d=C._get_sth(c,O);Y=I.loads(d.text);Z={}
		if Y.get(M)==0:
			D=Y[E];C.detailContent_args[V]=S=A(D['uid']);C.get_up_info_event.clear();C.pool.submit(C.get_up_info,S);e=D[R].replace(k,B).replace(l,B);g=D.get(Cc);h=D.get('description');i=D.get('parent_area_name')+'--'+D.get('area_name');G=D.get(CY,B)
			if G:G='开播时间：'+D.get('live_time')
			else:G='未开播'
			J={Q:F,P:e,U:g,BJ:i,C9:B,CA:'bililivedanmu',Ba:'房间号：'+F+Cx+S+Aa+G,Ab:h};T=B;a=B
			if C.userid:T='关注Ta';j=Cw;m=Cs;n=Ct;p=[j,m,n];a=N.join(p)
			L=X.result().get('From',[]);W=X.result().get(o,[])
			if L:q='API_1';r='flv线路原画$platform=web&quality=4_'+F+'#flv线路高清$platform=web&quality=3_'+F+'#h5线路原画$platform=h5&quality=4_'+F+'#h5线路高清$platform=h5&quality=3_'+F;L.append(q);W.append(r)
			if T:L.insert(1,T);W.insert(1,a)
			J[AN]=f.join(L);J[AO]=f.join(W);C.get_up_info_event.wait();b=C.up_info[S];J[CB]='🆙 '+b[K]+Cu+C.zh(D.get(Ci))+Aa+b[Ah];Z[H]=[J]
		return Z
	search_key=B
	def searchContent(A,key,quick):
		F=quick
		if not A.session_fake.cookies:A.pool.submit(A.getFakeCookie,AG)
		for C in A.task_pool:C.cancel()
		A.task_pool=[];A.search_key=key;E=A.detailContent_args.get(V,B)
		if F and E:G=A.pool.submit(A.get_up_videos,E,1,Ce)
		I={AB:B,C_:'番剧: ',D0:'影视: ',C6:'用户: ',AW:'直播: '}
		for(type,J)in I.items():C=A.pool.submit(A.get_search_content,key=key,pg=J,duration_diff=0,order=B,type=type,ps=A.userConfig[Y]);A.task_pool.append(C)
		D={H:[]}
		for C in Bi(A.task_pool):K=C.result().get(H,[]);D[H].extend(K);A.task_pool.remove(C)
		if F:
			if E:D[H]=A.detailContent_args.get(CC,[])+G.result().get(H,[])+A.detailContent_args.get(Cp,[])+D[H]
			else:D[H]=A.detailContent_args.get(B5,[])+D[H]
		return D
	stop_heartbeat_event=j.Event()
	def start_heartbeat(C,aid,cid,ids):
		N=aid;L=cid;M=P=S=B
		for G in ids:
			if q in G:P=G.replace(q,B)
			elif z in G:S=G.replace(z,B)
			elif CG in G:M=F(G.replace(CG,B))
		H='https://api.bilibili.com/x/player/v2?aid={0}&cid={1}'.format(N,L);Q=C._get_sth(H);X=I.loads(Q.text);D=X.get(E,{});T=D.get(CC,{})
		if T.get(B8):
			U=T.get(B8);Y=C.detailContent_args.get(B8)
			if Y!=U:C.detailContent_args[B8]=U;C.pool.submit(C.interaction_detailContent)
		R=F(C.userConfig[BD])
		if not C.userid or not R:return
		if not M:H='https://api.bilibili.com/x/web-interface/view?aid={0}&cid={1}'.format(N,L);Q=C._get_sth(H,O);Z=I.loads(Q.text);M=Z[E][e]
		J=0
		if F(D.get('last_play_cid',0))==F(L):
			V=F(D.get('last_play_time'))
			if V>0:J=F(V/1000)
		W=F((M-J)/R)+1;H='https://api.bilibili.com/x/click-interface/web/heartbeat';D={a:A(N),n:A(L),CH:A(C.csrf)}
		if P:D['sid']=A(P);D['epid']=A(S);D[r]=AV
		K=0;C.stop_heartbeat_event.clear()
		while AG:
			if K==R or C.stop_heartbeat_event.is_set():J+=K;K=0
			if not K:
				W-=1
				if not W:J=-1;C.stop_heartbeat_event.set()
				D['played_time']=A(J);C.pool.submit(C._post_sth,url=H,data=D)
				if C.stop_heartbeat_event.is_set():break
			x.sleep(1);K+=1
	wbi_key={}
	def get_wbiKey(A,wts):D='wbi_img';C=A.fetch(CT,headers=A.header);F=C.json()[E][D]['img_url'];G=C.json()[E][D]['sub_url'];H=[46,47,18,2,53,8,23,32,15,50,10,31,58,3,45,35,27,43,5,49,33,9,42,19,29,28,14,39,12,38,41,13,37,48,7,16,24,55,40,61,26,17,0,1,60,51,30,4,22,25,54,21,56,59,6,63,57,62,11,36,20,34,44,52];I=F.split(AA)[-1].split('.')[0]+G.split(AA)[-1].split('.')[0];J=reduce(lambda s,i:s+I[i],H,B);A.wbi_key={S:J[:32],CI:wts}
	def encrypt_wbi(D,**C):
		E=Bj(x.time())
		if not D.wbi_key or abs(D.wbi_key[CI])<30:D.get_wbiKey(E)
		C[CI]=E;C=A2(sorted(C.items()));C={C:B.join(filter(lambda chr:chr not in"!'()*",A(D)))for(C,D)in C.items()};F=CL(C);return F+'&w_rid='+hashlib.md5((F+D.wbi_key[S]).encode(encoding=As)).hexdigest()
	def _get_sth(A,url,_type=h):
		D=_type;B=url
		if D==AS and A.session_vip.cookies:C=A.session_vip.get(B,headers=A.header)
		elif D==O:
			if not A.session_fake.cookies:A.getFakeCookie_event.wait()
			C=A.session_fake.get(B,headers=A.header)
		else:C=A.session_master.get(B,headers=A.header)
		return C
	def _post_sth(A,url,data):return A.session_master.post(url,headers=A.header,data=data)
	def post_live_history(B,room_id):C={Cl:A(room_id),'platform':'pc',CH:A(B.csrf)};D='https://api.live.bilibili.com/xlive/web-room/v1/index/roomEntryAction';B._post_sth(url=D,data=C)
	def do_notplay(F,ids):
		C=ids;G=F.detailContent_args.get(a);H=F.detailContent_args.get(V);I=F.detailContent_args.get(B6);D={CH:A(F.csrf)};E=B
		if CJ in C:F.detailContent_args[CJ]=A(C[0]);return
		elif'follow'in C:
			if C2 in C:D.update({'fids':A(H),'tagids':A(C[0])});E='https://api.bilibili.com/x/relation/tags/addUsers'
			else:D.update({'fid':A(H),'act':A(C[0])});E='https://api.bilibili.com/x/relation/modify'
		elif'zhui'in C:D.update({AX:A(I)});E='https://api.bilibili.com/pgc/web/follow/'+A(C[0])
		elif B2 in C:D.update({a:A(G),B2:A(C[0])});E='https://api.bilibili.com/x/web-interface/archive/like'
		elif Bz in C:D.update({a:A(G),'multiply':A(C[0]),'select_like':T});E='https://api.bilibili.com/x/web-interface/coin/add'
		elif'fav'in C:D.update({'rid':A(G),r:A0});D[C[1]+'_media_ids']=A(C[0]);E='https://api.bilibili.com/x/v3/fav/resource/deal'
		elif'triple'in C:D.update({a:A(G)});E='https://api.bilibili.com/x/web-interface/archive/like/triple'
		elif'reply'in C:D.update({'oid':A(C[0]),'rpid':A(C[1]),r:T,'action':T});E='http://api.bilibili.com/x/v2/reply/action'
		F._post_sth(url=E,data=D)
	def get_cid(D,video):
		C=video;F='https://api.bilibili.com/x/web-interface/view?aid=%s'%A(C[a]);G=D._get_sth(F);H=I.loads(G.text);B=H[E];C[n]=B[n];C[e]=B[e]
		if BZ in B and B_ in B[BZ]:C[z]=D.find_bangumi_id(B[BZ])
	cookie_dic_tmp={}
	def get_cookies(A,key):
		D='https://passport.bilibili.com/x/passport-login/web/qrcode/poll?qrcode_key='+key;F=A._get_sth(D,O);B=I.loads(F.text)
		if B[M]==0:
			C=B[E][Cn]
			if not C:A.cookie_dic_tmp[key]=A2(A.session_fake.cookies);A.pool.submit(A.getFakeCookie)
			return C
		return'网络错误'
	def set_cookie(A,key,_type):
		D=_type;C=key;F=A.cookie_dic_tmp.get(C,B)
		if not F:
			G=A.get_cookies(C)
			if G:return
		E=A.userConfig.get(c,{});E[D]={A4:A.cookie_dic_tmp.get(C,{})};A.userConfig.update({c:E});A.getCookie(D);A.dump_config()
	def unset_cookie(A,_type):
		C=_type
		if C==AS:A.session_vip.cookies.clear()
		else:A.session_master.cookies=A.session_fake.cookies;A.userid=A.csrf=B
		if C in A.userConfig.get(c,{}):A.userConfig[c].pop(C);A.dump_config()
	def set_normal_default(B,id,type):B.userConfig[type]=A(id);B.dump_config()
	def set_normal_cateManual(B,name,_List,action):
		H=action;F=name;E=_List;G=B.userConfig.get(A(E)+AE)
		if not G:G=B.userConfig[A(E)+AE]=[]
		if H=='save':
			for I in B.defaultConfig[E]:
				if not I in G.copy():B.userConfig[A(E)+AE].append(I)
			B.userConfig[E]=B.userConfig[A(E)+AE].copy();B.userConfig.pop(E+AE);B.dump_config()
		elif H=='clear':B.userConfig[E]=B.defaultConfig[E].copy();B.userConfig.pop(A(E)+AE);B.dump_config()
		else:
			if E==y:
				F=F.split(Am)
				if W(F)==3:F[1]+=J+A(F[2])
				F={D:F[0],C:A(F[1])}
			if F in G:B.userConfig[A(E)+AE].remove(F)
			else:B.userConfig[A(E)+AE].append(F)
	def add_cateManualLiveExtra(A,action,name,id):
		F='cateManualLive_tmp';G=A.userConfig.get(A5,[])
		if not G:G=A.userConfig[A5]=[]
		if action=='clear':
			for E in G:
				E[C]=E[C].replace(Am,J)
				if E in A.userConfig.get(y,[]):A.userConfig[y].remove(E)
				if E in A.userConfig.get(F,[]):A.userConfig[F].remove(E)
			A.userConfig.pop(A5)
		elif id in s(g(lambda x:x[C],A.userConfig.get(A5,[]))):
			B={D:name,C:id};A.userConfig[A5].remove(B);B[C]=id.replace(Am,J)
			if B in A.userConfig.get(y,[]):A.userConfig[y].remove(B)
			if B in A.userConfig.get(F,[]):A.userConfig[F].remove(B)
		else:B={D:name,C:id};A.userConfig[A5].append(B)
		A.dump_config()
	def _checkUpdate(A,action):
		E={A9:A.header[A9]}
		if F(action):
			D=A.userConfig.get(AP)
			if D and D[CE]!=A.userConfig[Bk]:
				A.userConfig[AP][Bb]='正在更新';B=D[o];C=Bh(url=B,headers=E,timeout=(3,5))
				if C.status_code==200:
					H=B.split(AA)
					with BB(f"{AF}/{H[-1]}",'w',encoding=As)as J:J.write(C.text)
					A.userConfig[AP][Bb]='更新完成'
				else:A.userConfig[AP][Bb]='更新失败'
		else:
			B=A.mirror_site+CV;C=A.fetch(B,headers=E);G=I.loads(C.text);K=G.get(CE)
			if K:A.userConfig[AP]=G
	vod_qn_id={'127':'8K','126':'杜比视界','125':'HDR','120':'4K','116':'1080P60帧','112':'1080P+','80':'1080P','64':'720P'};vod_codec_id={'7':'avc','12':'hevc','13':'av1'};vod_audio_id={'30280':D1,'30232':'132000','30216':'64000'}
	def get_dash_media(I,video):
		H='SegmentBase';B=video;C=A(B.get(m));D=B.get(D2);K=B.get('codecs');L=B.get('bandwidth');M=B.get('startWithSap');E=B.get(D3);N=B.get('baseUrl').replace('&','&amp;');O=B[H].get('indexRange');P=B[H].get('Initialization');F=E.split(AA)[0]
		if F==AB:Q=B.get('frameRate');R=B.get('sar');S=B.get('width');T=B.get('height');G=f"height='{T}' width='{S}' frameRate='{Q}' sar='{R}'"
		elif F==Be:U=I.vod_audio_id.get(C,D1);G=f"numChannels='2' sampleRate='{U}'"
		if D:C+=J+A(D)
		V=f'''
      <Representation id="{C}" bandwidth="{L}" codecs="{K}" mimeType="{E}" {G} startWithSAP="{M}">
        <BaseURL>{N}</BaseURL>
        <SegmentBase indexRange="{O}">
          <Initialization range="{P}"/>
        </SegmentBase>
      </Representation>''';return V
	def get_dash_media_list(I,media_lis):
		D=media_lis
		if not D:return B
		E=D[0][D3].split(AA)[0];C=N=B
		if E==AB:
			C=K=I.detailContent_args.get(CJ,B)
			if K:K=F(K)
			else:C=A(I.userConfig[An]);K=120
			N=A(I.userConfig[Bn])
		elif E==Be:C=A(I.userConfig[Ao]);K=F(C);N=L
		G=s(g(lambda x:A(x[m])+J+A(x[D2]),D));H=[]
		if C+J+N in G:H.append(D[G.index(C+J+N)])
		if not H and E==AB:
			for Q in I.vod_codec_id.keys():
				if C+J+A(Q)in G:H.append(D[G.index(C+J+A(Q))])
		if not H:
			M=B
			for P in G:
				O=P.split(J)
				if M and F(M)>F(O[0]):break
				elif E==AB and F(O[0])<=K and not M or E==Be and not M or F(O[0])==M:
					M=F(O[0])
					if E==AB and A(O[1])==N:H=[D[G.index(A(P))]];break
					H.append(D[G.index(A(P))])
		R=f'\n    <AdaptationSet>\n      <ContentComponent contentType="{E}"/>{B.join(g(I.get_dash_media,H))}\n    </AdaptationSet>';return R
	get_dash_event=j.Event()
	def get_dash(A,ja):
		B=ja.get(e);C=ja.get('minBufferTime');D=A.pool.submit(A.get_dash_media_list,ja.get(AB));E=A.pool.submit(A.get_dash_media_list,ja.get(Be));F=f'<MPD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:mpeg:dash:schema:mpd:2011" xsi:schemaLocation="urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd" type="static" mediaPresentationDuration="PT{B}S" minBufferTime="PT{C}S" profiles="urn:mpeg:dash:profile:isoff-on-demand:2011">\n  <Period duration="PT{B}S" start="PT0S">{D.result()}{E.result()}\n  </Period>\n</MPD>'
		with BB(f"{AF}/playurl.mpd",'w',encoding=As)as G:G.write(F)
		A.get_dash_event.set();x.sleep(3);os.remove(f"{AF}/playurl.mpd")
	def get_durl(I,ja):
		H='size';C=-1;A=-1
		for D in range(W(ja)):
			E=ja[D]
			if C<F(E[H]):C=F(E[H]);A=D
		G=B
		if W(ja)>0:
			if A==-1:A=0
			G=ja[A][o]
		return G
	def playerContent(C,flag,id,vipFlags):
		C.stop_heartbeat_event.set();D={D4:B,o:B};F=id.split(J)
		if'web'in id or D5==F[0]:return C.live_playerContent(flag,id,vipFlags)
		if W(F)<2:return D
		H=F[0];G=F[1]
		if Cq in F:
			if'liveFilter'in id:id=F[2];C.add_cateManualLiveExtra(H,G,id)
			elif G==CD:C._checkUpdate(H)
			elif G in[Aq,y,BE,BF]:S=F[2];C.set_normal_cateManual(H,G,S)
			elif'login'in id:C.set_cookie(H,G)
			elif'logout'in id:C.unset_cookie(H)
			else:C.set_normal_default(H,G)
			return D
		elif'notplay'in F:C.pool.submit(C.do_notplay,F);return D
		elif G==n:
			N={a:A(H)};C.get_cid(N);G=N[n];F.append(CG+A(N[e]));P=N.get(z)
			if P:id+=J+P;F.append(P)
		U=C.encrypt_wbi(avid=H,cid=G,fnval=4048,fnver=0,fourk=1);O=f"https://api.bilibili.com/x/player/wbi/playurl?{U}"
		if z in id:
			if Ak in id:V=s(A for A in g(lambda x:x if z in x else AU,F)if A is not AU);O='https://www.bilibili.com/bangumi/play/'+V[0];D[o]=O;D['flag']='bilibili';D[Ak]=T;D['jx']=T;D[CK]=A({A9:C.header[A9]});return D
			O='https://api.bilibili.com/pgc/player/web/playurl?aid={}&cid={}&fnval=4048&fnver=0&fourk=1'.format(H,G)
		X=C._get_sth(O,AS);K=I.loads(X.text)
		if K[M]==0:
			if E in K:Q=K[E]
			elif AM in K:Q=K[AM]
			else:return D
		else:return D
		R=Q.get('dash')
		if R:C.get_dash_event.clear();Y=C.pool.submit(C.get_dash,R);C.get_dash_event.wait();D[o]=f"{AF}/playurl.mpd"
		else:D[o]=C.get_durl(Q.get('durl',{}))
		D[Ak]=L;D[BA]=B;D[CK]=C.header;C.pool.submit(C.start_heartbeat,H,G,F);return D
	def live_playerContent(G,flag,id,vipFlags):
		U='video/x-flv';T='url_info';C={D4:B,o:B};D=id.split(J)
		if W(D)<2:return C
		if G.userid and F(G.userConfig[BD])>0:G.pool.submit(G.post_live_history,D[-1])
		if D[0]==D5:
			V=F(D[1]);format=F(D[2]);H=F(D[3]);X=F(D[-1]);P='https://api.live.bilibili.com/xlive/web-room/v2/index/getRoomPlayInfo?room_id={0}&protocol=0,1&format={1}&codec={2}&qn={3}&ptype=8&platform=web&dolby=5&panorama=1&no_playurl=0&mask=1'.format(X,format,H,V);Q=G._get_sth(P,O);K=I.loads(Q.text)
			if K[M]==0:
				try:N=K[E][Cy].get(CF);H=N[Cz][0][Bd][0][Bc][0]
				except:return C
				Y=A(H['base_url']);Z=A(H[T][0]['host']);a=A(H[T][0]['extra']);N=Z+Y+a;C[o]=N
				if'.flv'in N:C[BA]=U
				else:C[BA]=B
			else:return C
		else:
			P='https://api.live.bilibili.com/room/v1/Room/playUrl?cid=%s&%s'%(D[1],D[0])
			try:Q=G._get_sth(P)
			except:return C
			R=I.loads(Q.text)
			if R[M]==0:
				K=R[E];S=K['durl']
				if W(S)>0:C[o]=S[0][o]
				if'h5'in D[0]:C[BA]=B
				else:C[BA]=U
			else:return C
		C[Ak]=L;C[CK]={D6:'https://live.bilibili.com',A9:G.header[A9]};return C
	config={'player':{},Z:{BG:[{S:C5,K:'分类',G:[{D:B3,C:B3},{D:C0,C:C0},{D:B4,C:B4},{D:C1,C:C1},{D:'我的粉丝',C:'我的粉丝'}]}],AI:[{S:b,K:'个人动态排序',G:[{D:'最新发布',C:Ag},{D:'最多播放',C:'click'},{D:'最多收藏',C:'stow'},{D:'最早发布',C:Cd}]}],Ac:[{S:A1,K:'分类',G:[{D:'番剧',C:T},{D:'国创',C:AV},{D:'电影',C:A0},{D:'电视剧',C:'5'},{D:'纪录片',C:AQ},{D:'综艺',C:'7'}]},{S:b,K:'排序',G:[{D:A3,C:A3},{D:'播放数量',C:A0},{D:'更新时间',C:L},{D:'最高评分',C:AV},{D:'弹幕数量',C:T},{D:'追看人数',C:AQ},{D:'开播时间',C:'5'},{D:'上映时间',C:'6'}]},{S:C4,K:'付费',G:[{D:'全部',C:'-1'},{D:'免费',C:T},{D:'付费',C:'2%2C6'},{D:'大会员',C:'4%2C6'}]}],Ar:[{S:b,K:'排序',G:[{D:'近期热门',C:'hot'},{D:'月播放量',C:A_},{D:'最新投稿',C:'new'},{D:'频道精选',C:Ck}]}],Ad:[{S:b,K:'排序',G:[{D:'收藏时间',C:'mtime'},{D:'播放量',C:A_},{D:'投稿时间',C:'pubtime'}]}],BH:[{S:r,K:'分类',G:[{D:'视频',C:BO},{D:AH,C:AW},{D:BN,C:BN},{D:BU,C:BU}]}],BI:[{S:r,K:'类型',G:[{D:'视频',C:AB},{D:'番剧',C:C_},{D:Ac,C:D0},{D:AH,C:AW},{D:'用户',C:C6}]},{S:b,K:'视频排序',G:[{D:'综合排序',C:Cm},{D:'最新发布',C:Ag},{D:'最多点击',C:'click'},{D:'最多收藏',C:'stow'},{D:'最多弹幕',C:'dm'}]},{S:e,K:'视频时长',G:[{D:'全部',C:L},{D:'60分钟以上',C:AV},{D:'30~60分钟',C:AQ},{D:'5~30分钟',C:A0},{D:'5分钟以下',C:T}]}]}};header={'Origin':Bt,D6:Bt,A9:'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15'}
	def localProxy(A,param):return[200,'video/MP2T',action,B]