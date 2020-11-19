'use strict';/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var og=function(a,b,c){a.timeOfStartCall=(new Date).getTime();var d=c||Ea,e=d.document,f=a.nonce||Ha(d);f&&!a.nonce&&(a.nonce=f);if("help"==a.flow){var g=Ja("document.location.href",d);!a.helpCenterContext&&g&&(a.helpCenterContext=g.substring(0,1200));g=!0;if(b&&JSON&&JSON.stringify){var h=JSON.stringify(b);(g=1200>=h.length)&&(a.psdJson=h)}g||(b={invalidPsd:!0})}b=[a,b,c];d.GOOGLE_FEEDBACK_START_ARGUMENTS=b;c=a.serverUri||"//www.google.com/tools/feedback";if(g=d.GOOGLE_FEEDBACK_START)g.apply(d,b);
else{d=c+"/load.js?";for(var l in a)b=a[l],null==b||Pa(b)||(d+=encodeURIComponent(l)+"="+encodeURIComponent(b)+"&");a=cg(e);a=ig(a.g,"SCRIPT");f&&a.setAttribute("nonce",f);qe(a,new bd($c,d));e.body.appendChild(a)}};x("userfeedback.api.startFeedback",og);var pg=function(){this.j=this.h=this.s=this.modelName=this.l=this.g=this.ae="";this.o=this.w=this.m=!1};var qg=chrome.i18n.getMessage("4163185390680253103"),rg=chrome.i18n.getMessage("492097680647953484"),sg=chrome.i18n.getMessage("2575016469622936324"),tg=chrome.i18n.getMessage("128276876460319075"),ug=chrome.i18n.getMessage("3326722026796849289"),vg=chrome.i18n.getMessage("1018984561488520517"),wg=chrome.i18n.getMessage("8205999658352447129"),xg=chrome.i18n.getMessage("5723583529370342957"),yg=chrome.i18n.getMessage("1550904064710828958"),zg=chrome.i18n.getMessage("5014364904504073524"),Ag=chrome.i18n.getMessage("2194670894476780934"),
Bg=chrome.i18n.getMessage("6614468912728530636"),Cg=chrome.i18n.getMessage("5910595154486533449"),Dg=chrome.i18n.getMessage("5363086287710390513"),Eg=chrome.i18n.getMessage("244647017322945605"),Fg=chrome.i18n.getMessage("5375576275991472719"),Gg=chrome.i18n.getMessage("4592127349908255218"),Hg=chrome.i18n.getMessage("843316808366399491"),Ig=chrome.i18n.getMessage("5699813974548050528"),Jg=chrome.i18n.getMessage("8515148417333877999"),Kg=chrome.i18n.getMessage("1636686747687494376"),Lg=chrome.i18n.getMessage("4148300086676792937"),
Mg=chrome.i18n.getMessage("3219866268410307919"),Ng=chrome.i18n.getMessage("9211708838274008657"),Og=chrome.i18n.getMessage("8706273405040403641"),Pg=chrome.i18n.getMessage("4756056595565370923"),Qg=chrome.i18n.getMessage("7876724262035435114"),Rg=chrome.i18n.getMessage("5485620192329479690"),Sg=chrome.i18n.getMessage("6963873398546068901"),Tg=chrome.i18n.getMessage("3567591856726172993"),Ug=chrome.i18n.getMessage("3239956785410157548");var Vg={"* ARIA-CHECKED":!0,"* ARIA-COLCOUNT":!0,"* ARIA-COLINDEX":!0,"* ARIA-CONTROLS":!0,"* ARIA-DESCRIBEDBY":!0,"* ARIA-DISABLED":!0,"* ARIA-EXPANDED":!0,"* ARIA-GOOG-EDITABLE":!0,"* ARIA-HASPOPUP":!0,"* ARIA-HIDDEN":!0,"* ARIA-LABEL":!0,"* ARIA-LABELLEDBY":!0,"* ARIA-MULTILINE":!0,"* ARIA-MULTISELECTABLE":!0,"* ARIA-ORIENTATION":!0,"* ARIA-PLACEHOLDER":!0,"* ARIA-READONLY":!0,"* ARIA-REQUIRED":!0,"* ARIA-ROLEDESCRIPTION":!0,"* ARIA-ROWCOUNT":!0,"* ARIA-ROWINDEX":!0,"* ARIA-SELECTED":!0,"* ABBR":!0,
"* ACCEPT":!0,"* ACCESSKEY":!0,"* ALIGN":!0,"* ALT":!0,"* AUTOCOMPLETE":!0,"* AXIS":!0,"* BGCOLOR":!0,"* BORDER":!0,"* CELLPADDING":!0,"* CELLSPACING":!0,"* CHAROFF":!0,"* CHAR":!0,"* CHECKED":!0,"* CLEAR":!0,"* COLOR":!0,"* COLSPAN":!0,"* COLS":!0,"* COMPACT":!0,"* COORDS":!0,"* DATETIME":!0,"* DIR":!0,"* DISABLED":!0,"* ENCTYPE":!0,"* FACE":!0,"* FRAME":!0,"* HEIGHT":!0,"* HREFLANG":!0,"* HSPACE":!0,"* ISMAP":!0,"* LABEL":!0,"* LANG":!0,"* MAX":!0,"* MAXLENGTH":!0,"* METHOD":!0,"* MULTIPLE":!0,
"* NOHREF":!0,"* NOSHADE":!0,"* NOWRAP":!0,"* OPEN":!0,"* READONLY":!0,"* REQUIRED":!0,"* REL":!0,"* REV":!0,"* ROLE":!0,"* ROWSPAN":!0,"* ROWS":!0,"* RULES":!0,"* SCOPE":!0,"* SELECTED":!0,"* SHAPE":!0,"* SIZE":!0,"* SPAN":!0,"* START":!0,"* SUMMARY":!0,"* TABINDEX":!0,"* TITLE":!0,"* TYPE":!0,"* VALIGN":!0,"* VALUE":!0,"* VSPACE":!0,"* WIDTH":!0},Wg={"* USEMAP":!0,"* ACTION":!0,"* CITE":!0,"* HREF":!0,"* LONGDESC":!0,"* SRC":!0,"LINK HREF":!0,"* FOR":!0,"* HEADERS":!0,"* NAME":!0,"A TARGET":!0,
"* CLASS":!0,"* ID":!0,"* STYLE":!0};var Xg={};
function Yg(a){if(He&&!af(9))return[0,0,0,0];var b=Xg.hasOwnProperty(a)?Xg[a]:null;if(b)return b;65536<Object.keys(Xg).length&&(Xg={});var c=[0,0,0,0];b=Zg(a,/\\[0-9A-Fa-f]{6}\s?/g);b=Zg(b,/\\[0-9A-Fa-f]{1,5}\s/g);b=Zg(b,/\\./g);b=b.replace(/:not\(([^\)]*)\)/g,"     $1 ");b=b.replace(/{[^]*/gm,"");b=$g(b,c,/(\[[^\]]+\])/g,2);b=$g(b,c,/(#[^\#\s\+>~\.\[:]+)/g,1);b=$g(b,c,/(\.[^\s\+>~\.\[:]+)/g,2);b=$g(b,c,/(::[^\s\+>~\.\[:]+|:first-line|:first-letter|:before|:after)/gi,3);b=$g(b,c,/(:[\w-]+\([^\)]*\))/gi,2);
b=$g(b,c,/(:[^\s\+>~\.\[:]+)/g,2);b=b.replace(/[\*\s\+>~]/g," ");b=b.replace(/[#\.]/g," ");$g(b,c,/([^\s\+>~\.\[:]+)/g,3);b=c;return Xg[a]=b}function $g(a,b,c,d){return a.replace(c,function(e){b[d]+=1;return Array(e.length+1).join(" ")})}function Zg(a,b){return a.replace(b,function(c){return Array(c.length+1).join("A")})};var ah={rgb:!0,rgba:!0,alpha:!0,rect:!0,image:!0,"linear-gradient":!0,"radial-gradient":!0,"repeating-linear-gradient":!0,"repeating-radial-gradient":!0,"cubic-bezier":!0,matrix:!0,perspective:!0,rotate:!0,rotate3d:!0,rotatex:!0,rotatey:!0,steps:!0,rotatez:!0,scale:!0,scale3d:!0,scalex:!0,scaley:!0,scalez:!0,skew:!0,skewx:!0,skewy:!0,translate:!0,translate3d:!0,translatex:!0,translatey:!0,translatez:!0},bh=/[\n\f\r"'()*<>]/g,ch={"\n":"%0a","\f":"%0c","\r":"%0d",'"':"%22","'":"%27","(":"%28",")":"%29",
"*":"%2a","<":"%3c",">":"%3e"};function dh(a){return ch[a]}
var eh=function(a,b,c){b=jd(b);if(""==b)return null;if(0==kd("url(",b.substr(0,4))){if(!b.endsWith(")")||1<(b?b.split("(").length-1:0)||1<(b?b.split(")").length-1:0)||!c)a=null;else{a:{b=b.substring(4,b.length-1);for(var d=0;2>d;d++){var e="\"'".charAt(d);if(b.charAt(0)==e&&b.charAt(b.length-1)==e){b=b.substring(1,b.length-1);break a}}}a=c?(a=c(b,a))&&"about:invalid#zClosurez"!=zd(a)?'url("'+zd(a).replace(bh,dh)+'")':null:null}return a}if(0<b.indexOf("(")){if(/"|'/.test(b))return null;for(a=/([\-\w]+)\(/g;c=
a.exec(b);)if(!(c[1].toLowerCase()in ah))return null}return b};function fh(a,b){a=Ea[a];return a&&a.prototype?(b=Object.getOwnPropertyDescriptor(a.prototype,b))&&b.get||null:null}function gh(a,b){return(a=Ea[a])&&a.prototype&&a.prototype[b]||null}
var hh=fh("Element","attributes")||fh("Node","attributes"),ih=gh("Element","hasAttribute"),jh=gh("Element","getAttribute"),kh=gh("Element","setAttribute"),lh=gh("Element","removeAttribute"),mh=gh("Element","getElementsByTagName"),nh=gh("Element","matches")||gh("Element","msMatchesSelector"),oh=fh("Node","nodeName"),ph=fh("Node","nodeType"),qh=fh("Node","parentNode"),rh=fh("HTMLElement","style")||fh("Element","style"),sh=fh("HTMLStyleElement","sheet"),th=gh("CSSStyleDeclaration","getPropertyValue"),
uh=gh("CSSStyleDeclaration","setProperty");function vh(a,b,c,d){if(a)return a.apply(b);a=b[c];if(!d(a))throw Error("Clobbering detected");return a}function wh(a,b,c,d){if(a)return a.apply(b,d);if(He&&10>document.documentMode){if(!b[c].call)throw Error("IE Clobbering detected");}else if("function"!=typeof b[c])throw Error("Clobbering detected");return b[c].apply(b,d)}function xh(a){return vh(hh,a,"attributes",function(b){return b instanceof NamedNodeMap})}
function yh(a,b,c){try{wh(kh,a,"setAttribute",[b,c])}catch(d){if(-1==d.message.indexOf("A security problem occurred"))throw d;}}function zh(a){Ah(a);return vh(rh,a,"style",function(b){return b instanceof CSSStyleDeclaration})}function Ah(a){if(!(a instanceof HTMLElement))throw Error("Not an HTMLElement");}function Bh(a){Ah(a);return vh(sh,a,"sheet",function(b){return b instanceof CSSStyleSheet})}function Ch(a){return vh(oh,a,"nodeName",function(b){return"string"==typeof b})}
function Dh(a){return vh(ph,a,"nodeType",function(b){return"number"==typeof b})}function Eh(a){return vh(qh,a,"parentNode",function(b){return!(b&&"string"==typeof b.name&&b.name&&"parentnode"==b.name.toLowerCase())})}function Fh(a,b){return wh(th,a,a.getPropertyValue?"getPropertyValue":"getAttribute",[b])||""}function Gh(a,b,c){wh(uh,a,a.setProperty?"setProperty":"setAttribute",[b,c])};var Hh=He&&10>document.documentMode?null:/\s*([^\s'",]+[^'",]*(('([^'\r\n\f\\]|\\[^])*')|("([^"\r\n\f\\]|\\[^])*")|[^'",])*)/g,Ih={"-webkit-border-horizontal-spacing":!0,"-webkit-border-vertical-spacing":!0},Lh=function(a,b,c){var d=[];a=Jh(cc(a.cssRules));Hb(a,function(e){if(b&&!/[a-zA-Z][\w-:\.]*/.test(b))throw Error("Invalid container id");if(!(b&&He&&10==document.documentMode&&/\\['"]/.test(e.selectorText))){var f=b?e.selectorText.replace(Hh,"#"+b+" $1"):e.selectorText;d.push(Sd(f,Kh(e.style,
c)))}});return Ud(d)},Jh=function(a){return Jb(a,function(b){return b instanceof CSSStyleRule||b.type==CSSRule.STYLE_RULE})},Nh=function(a,b,c){a=Mh("<style>"+a+"</style>");return null==a||null==a.sheet?Vd:Lh(a.sheet,void 0!=b?b:null,c)},Mh=function(a){if(He&&!af(10)||"function"!=typeof Ea.DOMParser)return null;a=je("<html><head></head><body>"+a+"</body></html>",null);return(new DOMParser).parseFromString(ie(a),"text/html").body.children[0]},Kh=function(a,b){if(!a)return Gd;var c=document.createElement("div").style,
d=Oh(a);Hb(d,function(e){var f=Ke&&e in Ih?e:e.replace(/^-(?:apple|css|epub|khtml|moz|mso?|o|rim|wap|webkit|xv)-(?=[a-z])/i,"");gd(f,"--")||gd(f,"var")||(e=Fh(a,e),e=eh(f,e,b),null!=e&&Gh(c,f,e))});return Fd(c.cssText||"")},Qh=function(a){var b=Array.from(wh(mh,a,"getElementsByTagName",["STYLE"])),c=oc(b,function(e){return cc(Bh(e).cssRules)});c=Jh(c);c.sort(function(e,f){e=Yg(e.selectorText);a:{f=Yg(f.selectorText);for(var g=hc,h=Math.min(e.length,f.length),l=0;l<h;l++){var p=g(e[l],f[l]);if(0!=
p){e=p;break a}}e=hc(e.length,f.length)}return-e});a=document.createTreeWalker(a,NodeFilter.SHOW_ELEMENT,null,!1);for(var d;d=a.nextNode();)Hb(c,function(e){wh(nh,d,d.matches?"matches":"msMatchesSelector",[e.selectorText])&&e.style&&Ph(d,e.style)});Hb(b,kg)},Ph=function(a,b){var c=Oh(a.style),d=Oh(b);Hb(d,function(e){if(!(0<=c.indexOf(e))){var f=Fh(b,e);Gh(a.style,e,f)}})},Oh=function(a){Na(a)?a=cc(a):(a=Dc(a),Zb(a,"cssText"));return a};var Rh="undefined"!=typeof WeakMap&&-1!=WeakMap.toString().indexOf("[native code]"),Sh=0,Th=function(){this.j=[];this.h=[];this.g="data-elementweakmap-index-"+Sh++};Th.prototype.set=function(a,b){if(wh(ih,a,"hasAttribute",[this.g])){var c=parseInt(wh(jh,a,"getAttribute",[this.g])||null,10);this.h[c]=b}else c=this.h.push(b)-1,yh(a,this.g,c.toString()),this.j.push(a);return this};
Th.prototype.get=function(a){if(wh(ih,a,"hasAttribute",[this.g]))return a=parseInt(wh(jh,a,"getAttribute",[this.g])||null,10),this.h[a]};Th.prototype.clear=function(){this.j.forEach(function(a){wh(lh,a,"removeAttribute",[this.g])},this);this.j=[];this.h=[]};var Uh=Wf("goog.html.sanitizer.SafeDomTreeProcessor"),Vh=!He||10<=Number(df),Wh=!He||null==document.documentMode,Xh=function(){};var Yh={APPLET:!0,AUDIO:!0,BASE:!0,BGSOUND:!0,EMBED:!0,FORM:!0,IFRAME:!0,ISINDEX:!0,KEYGEN:!0,LAYER:!0,LINK:!0,META:!0,OBJECT:!0,SCRIPT:!0,SVG:!0,STYLE:!0,TEMPLATE:!0,VIDEO:!0};var Zh={A:!0,ABBR:!0,ACRONYM:!0,ADDRESS:!0,AREA:!0,ARTICLE:!0,ASIDE:!0,B:!0,BDI:!0,BDO:!0,BIG:!0,BLOCKQUOTE:!0,BR:!0,BUTTON:!0,CAPTION:!0,CENTER:!0,CITE:!0,CODE:!0,COL:!0,COLGROUP:!0,DATA:!0,DATALIST:!0,DD:!0,DEL:!0,DETAILS:!0,DFN:!0,DIALOG:!0,DIR:!0,DIV:!0,DL:!0,DT:!0,EM:!0,FIELDSET:!0,FIGCAPTION:!0,FIGURE:!0,FONT:!0,FOOTER:!0,FORM:!0,H1:!0,H2:!0,H3:!0,H4:!0,H5:!0,H6:!0,HEADER:!0,HGROUP:!0,HR:!0,I:!0,IMG:!0,INPUT:!0,INS:!0,KBD:!0,LABEL:!0,LEGEND:!0,LI:!0,MAIN:!0,MAP:!0,MARK:!0,MENU:!0,METER:!0,NAV:!0,
NOSCRIPT:!0,OL:!0,OPTGROUP:!0,OPTION:!0,OUTPUT:!0,P:!0,PRE:!0,PROGRESS:!0,Q:!0,S:!0,SAMP:!0,SECTION:!0,SELECT:!0,SMALL:!0,SOURCE:!0,SPAN:!0,STRIKE:!0,STRONG:!0,STYLE:!0,SUB:!0,SUMMARY:!0,SUP:!0,TABLE:!0,TBODY:!0,TD:!0,TEXTAREA:!0,TFOOT:!0,TH:!0,THEAD:!0,TIME:!0,TR:!0,TT:!0,U:!0,UL:!0,VAR:!0,WBR:!0};var $h={"ANNOTATION-XML":!0,"COLOR-PROFILE":!0,"FONT-FACE":!0,"FONT-FACE-SRC":!0,"FONT-FACE-URI":!0,"FONT-FACE-FORMAT":!0,"FONT-FACE-NAME":!0,"MISSING-GLYPH":!0},di=function(a){a=a||new ai;bi(a);this.g=Ic(a.g);this.m=Ic(a.F);this.j=Ic(a.G);this.s=a.D;Hb(a.o,function(b){if(!gd(b,"data-"))throw new Db('Only "data-" attributes allowed, got: %s.',[b]);if(gd(b,"data-sanitizer-"))throw new Db('Attributes with "%s" prefix are not allowed, got: %s.',["data-sanitizer-",b]);this.g["* "+b.toUpperCase()]=ci},
this);Hb(a.w,function(b){b=b.toUpperCase();if(-1==b.indexOf("-")||$h[b])throw new Db("Only valid custom element tag names allowed, got: %s.",[b]);this.j[b]=!0},this);this.o=a.j;this.l=a.C;this.h=null;this.w=a.s};y(di,Xh);
var ei=function(a){return function(b,c){return(b=a(jd(b),c))&&"about:invalid#zClosurez"!=zd(b)?zd(b):null}},ai=function(){this.g={};Hb([Vg,Wg],function(a){Hb(Dc(a),function(b){this.g[b]=ci},this)},this);this.h={};this.o=[];this.w=[];this.F=Ic(Yh);this.G=Ic(Zh);this.D=!1;this.L=Bd;this.H=this.m=this.K=this.j=rc;this.C=null;this.l=this.s=!1},fi=function(a,b){return function(c,d,e,f){c=a(c,d,e,f);return null==c?null:b(c,d,e,f)}},gi=function(a,b,c,d){a[c]&&!b[c]&&(a[c]=fi(a[c],d))};ai.prototype.ha=function(){return new di(this)};
var bi=function(a){if(a.l)throw Error("HtmlSanitizer.Builder.build() can only be used once.");gi(a.g,a.h,"* USEMAP",hi);var b=ei(a.L);Hb(["* ACTION","* CITE","* HREF"],function(d){gi(this.g,this.h,d,b)},a);var c=ei(a.j);Hb(["* LONGDESC","* SRC","LINK HREF"],function(d){gi(this.g,this.h,d,c)},a);Hb(["* FOR","* HEADERS","* NAME"],function(d){gi(this.g,this.h,d,Wa(ii,this.K))},a);gi(a.g,a.h,"A TARGET",Wa(ji,["_blank","_self"]));gi(a.g,a.h,"* CLASS",Wa(ki,a.m));gi(a.g,a.h,"* ID",Wa(li,a.m));gi(a.g,a.h,
"* STYLE",Wa(a.H,c));a.l=!0},mi=function(a,b){a||(a="*");return(a+" "+b).toUpperCase()},ci=function(a){return jd(a)},ji=function(a,b){b=jd(b);return Tb(a,b.toLowerCase())?b:null},hi=function(a){return(a=jd(a))&&"#"==a.charAt(0)?a:null},ii=function(a,b,c){return a(jd(b),c)},ki=function(a,b,c){b=b.split(/(?:\s+)/);for(var d=[],e=0;e<b.length;e++){var f=a(b[e],c);f&&d.push(f)}return 0==d.length?null:d.join(" ")},li=function(a,b,c){return a(jd(b),c)},ni=function(a,b){var c=b.data;(b=Eh(b))&&"style"==
Ch(b).toLowerCase()&&!("STYLE"in a.m)&&"STYLE"in a.j&&(c=Td(Nh(c,a.h,w(function(d,e){return this.o(d,{uK:e})},a))));return document.createTextNode(c)},oi=function(a){var b=(new ai).ha();var c=!("STYLE"in b.m)&&"STYLE"in b.j;c="*"==b.l&&c?"sanitizer-"+we():b.l;b.h=c;if(Vh){c=a;if(Vh){a=ig(document,"SPAN");b.h&&"*"==b.l&&(a.id=b.h);b.w&&(c=Mh("<div>"+c+"</div>"),Qh(c),c=c.innerHTML);c=je(c,null);var d=document.createElement("template");if(Wh&&"content"in d)oe(d,c),d=d.content;else{var e=document.implementation.createHTMLDocument("x");
d=e.body;oe(e.body,c)}c=document.createTreeWalker(d,NodeFilter.SHOW_ELEMENT|NodeFilter.SHOW_TEXT,null,!1);for(d=Rh?new WeakMap:new Th;e=c.nextNode();){c:{var f=b;var g=e;var h=Dh(g);switch(h){case 3:g=ni(f,g);break c;case 1:h=g;1==Dh(h)||Eb("Expected Node of type Element but got Node of type %s",Dh(h));g=f;f=h;if("TEMPLATE"==Ch(f).toUpperCase())g=null;else{h=Ch(f).toUpperCase();if(h in g.m)var l=null;else g.j[h]?l=document.createElement(h):(l=ig(document,"SPAN"),g.s&&yh(l,"data-sanitizer-original-tag",
h.toLowerCase()));if(l){var p=l,r=xh(f);if(null!=r)for(var t=0;h=r[t];t++)if(h.specified){var A=g;var z=f,G=h,N=G.name;if(gd(N,"data-sanitizer-"))A=null;else{var Aa=Ch(z);G=G.value;var Mb={tagName:jd(Aa).toLowerCase(),attributeName:jd(N).toLowerCase()},Nb={zr:void 0};"style"==Mb.attributeName&&(Nb.zr=zh(z));z=mi(Aa,N);z in A.g?(A=A.g[z],A=A(G,Mb,Nb)):(N=mi(null,N),N in A.g?(A=A.g[N],A=A(G,Mb,Nb)):A=null)}null!==A&&yh(p,h.name,A)}g=l}else g=null}break c;default:C(Uh,"Dropping unknown node type: "+
h),g=null}}if(g){if(1==Dh(g)&&d.set(e,g),e=Eh(e),f=!1,e)h=Dh(e),l=Ch(e).toLowerCase(),p=Eh(e),11!=h||p?"body"==l&&p&&(h=Eh(p))&&!Eh(h)&&(f=!0):f=!0,h=null,f||!e?h=a:1==Dh(e)&&(h=d.get(e)),h.content&&(h=h.content),h.appendChild(g)}else jg(e)}d.clear&&d.clear();b=a}else b=ig(document,"SPAN");0<xh(b).length&&(a=ig(document,"SPAN"),a.appendChild(b),b=a);b=(new XMLSerializer).serializeToString(b);b=b.slice(b.indexOf(">")+1,b.lastIndexOf("</"))}else b="";return je(b,null)};if("undefined"!=typeof angular){var pi=angular.module("chrome_18n",[]);chrome.runtime&&chrome.runtime.getManifest&&chrome.runtime.getManifest().default_locale&&pi.directive("angularMessage",function(){return{restrict:"E",replace:!0,controller:["$scope",function(a){var b=this;this.Pi=this.ue=null;a.dirForText=function(c){b.ue||(b.ue=chrome.i18n.getMessage("@@bidi_dir")||"ltr");b.Pi||(b.Pi=new mg("rtl"==b.ue));var d=b.Pi,e,f=e=0,g=!1;c=(c||"").split(Yc);for(var h=0;h<c.length;h++){var l=c[h];Wc.test(l)?
(e++,f++):Xc.test(l)?g=!0:Vc.test(l)?f++:Zc.test(l)&&(g=!0)}e=0==f?g?1:0:.4<e/f?-1:1;return-1==(0==e?d.g:e)?"rtl":"ltr"}}],compile:function(a,b){b=b.key;var c=null,d=document.createElement("amr");b&&!b.match(/^\d+$/)&&(b=chrome.i18n.getMessage(b),null==b&&d.setAttribute("id","missing"));if(b){var e=chrome.i18n.getMessage(b+"_ph");c=[];if(null!=e)for(c=e.split("\ue000"),e=0;e<c.length;++e)c[e]=c[e].replace(/^{{(.*)}}$/,'<amrp dir="{{dirForText($1)}}">{{$1}}</amrp>');c=chrome.i18n.getMessage(b,c)}else d.setAttribute("r",
"nokey");c?pe(d,oi(c)):(d.setAttribute("tl","false"),pe(d,oi(a.html())));a.replaceWith(d)}}})};var ri=function(a,b){var c=this;this.w=b;this.g=a;this.g.top=a;this.o=[];this.l=!1;this.h=new pg;this.g.videoSmoothnessRatings=this.fl(Ag,vg,wg,xg,yg,zg);this.g.videoQualityRatings=this.fl(Ag,Bg,Cg,Dg,Eg,Fg);this.g.audioQualityRatings=this.fl(Ag,Gg,Hg,Ig,Jg,Kg);this.o=[{value:"Bug",desc:qg},{value:"FeatureRequest",desc:rg},{value:"MirroringQuality",desc:sg},{value:"Discovery",desc:tg},{value:"Other",desc:ug}];this.g.feedbackTypes=this.o;this.g.includeFineLogs=!0;this.g.feedbackType="Bug";this.g.sendFeedback=
this.Lv.bind(this);this.g.cancel=this.rr.bind(this);this.g.attachLogsClick=this.m.bind(this);this.g.viewLogs=this.C.bind(this);this.g.$watchGroup("videoSmoothness videoQuality audioQuality feedbackDescription comments feedbackType".split(" "),this.ur.bind(this));this.g.sufficientFeedback=!1;this.g.$watch("attachLogs",this.m.bind(this));this.g.attachLogs=!0;this.s=we();this.g.userEmail="";chrome.identity.getProfileUserInfo(function(d){c.g.userEmail=d.email;qi(c)});this.g.yourAnswerText=Ug;this.g.language=
chrome.i18n&&chrome.i18n.getUILanguage?chrome.i18n.getUILanguage():chrome.runtime.getManifest().default_locale;this.g.requestLogsInProgress=!1;this.g.mrVersion=chrome.runtime.getManifest().version};k=ri.prototype;k.fl=function(a){for(var b=[],c=1;c<arguments.length;c++)b.push(new si(c,arguments[c]));b.push(new si(0,arguments[0]));return b};k.rr=function(){this.g.feedbackDescription&&!confirm(Lg)||window.close()};
k.ur=function(){var a=this.g.feedbackType;this.g.sufficientFeedback="MirroringQuality"==a?this.g.videoSmoothness||this.g.videoQuality||this.g.audioQuality||this.g.comments:"Discovery"==a?this.g.visibleInSetup||this.g.comments:!!this.g.feedbackDescription};
k.Lv=function(){if(this.g.sufficientFeedback){var a=this.g.feedbackType,b="";"MirroringQuality"==a?(this.g.videoSmoothness&&(b+="\nVideo Smoothness: "+this.g.videoSmoothness),this.g.videoQuality&&(b+="\nVideo Quality: "+this.g.videoQuality),this.g.audioQuality&&(b+="\nAudio: "+this.g.audioQuality),this.g.projectedContentUrl&&(b+="\nProjected Content/URL: "+this.g.projectedContentUrl),this.g.comments&&(b+="\nComments: "+this.g.comments)):"Discovery"==a?(this.g.visibleInSetup&&(b+="\nChromecast Visible in Setup: "+
this.g.visibleInSetup),this.g.hasNetworkSoftware&&(b+="\nUsing VPN/proxy/firewall/NAS Software: "+this.g.hasNetworkSoftware),this.g.networkDescription&&(b+="\nNetwork Description: "+this.g.networkDescription),this.g.comments&&(b+="\nComments: "+this.g.comments)):b=this.g.feedbackDescription;a="Type: "+a+"\n\n"+b;this.g.sendDialogText=Mg;this.g.okButton=Tg;this.g.feedbackSent=!1;this.w.show({locals:{zK:this.g.feedbackSent,aL:this.g.sendDialogText,Rt:this.g.okButton},scope:this.g,preserveScope:!0,bindToController:!0,
template:'<md-dialog id="feedback-confirmation"><md-dialog-content><div id="send-feedback-text">{{sendDialogText}}</div><md-dialog-actions><md-button class="md-raised md-primary"ng-disabled="!feedbackSent" ng-click="closeWindow()">{{okButton}}</md-button></md-dialog-actions></md-dialog-content></md-dialog>',controller:this.j});this.zo(a,Date.now())}};k.zo=function(a,b){var c=Date.now();!this.g.requestLogsInProgress||5E3<c-b?ti(this,a):setTimeout(this.zo.bind(this),1E3,a,b)};
var ti=function(a,b){var c=0,d=function(f,g,h){h?f(!0):(a.g.sendDialogText=Pg,qi(a),g(Error("Failed to send")))},e=chrome.declarativeWebRequest?"MrTeamfood":"MRStable";(new mf(function(){c++;return new Promise(function(f,g){var h=a.g.userEmail,l=a.h;f=d.bind(null,f,g);g=chrome.runtime.getManifest();og({productId:85561,bucket:e,flow:"submit",serverUri:"https://www.google.com/tools/feedback",allowNonLoggedInFeedback:!0,locale:g.default_locale,enableAnonymousFeedback:!h,report:{description:b},callback:f},
{version:g.version,description:g.description,user_email:h||"NA",logs:l.ae||"NA",external_logs:l.g||"NA",device_model:l.modelName||"NA",receiver_version:l.s||"NA",dash_report_url:l.l||"NA",cast_device_counts:l.h,dial_device_counts:l.j,mirroring_service_enabled:l.m,native_cast_mrp_enabled:l.w,native_dial_mrp_enabled:l.o})})},1E4,4)).start().then(function(){ub("MediaRouter.Ui.Action.Feedback");a.g.sendDialogText=Og;a.g.feedbackSent=!0;qi(a)},function(){a.g.sendDialogText=Ng;a.g.feedbackSent=!0;qi(a)})};
ri.prototype.m=function(){var a=this;this.h=new pg;this.g.attachLogs&&(this.g.requestLogsInProgress=!0,chrome.runtime.sendMessage(new xf(this.s,"retrieve_log_data"),function(b){a.g.requestLogsInProgress=!1;a.h.ae=b.logs||"no extension";a.h.ae+="\n";a.h.ae+=b.mediaSinkServiceStatus||"no media sink service status from browser";b.castStreamingLogs&&(a.h.l=b.castStreamingLogs);b.castDeviceCounts&&(a.h.h=b.castDeviceCounts);b.dialDeviceCounts&&(a.h.j=b.dialDeviceCounts);a.h.m=!!b.mirroringServiceEnabled;
a.h.w=!!b.nativeCastMrpEnabled;a.h.o=!!b.nativeDialMrpEnabled;if(b=b.device)if(b.model&&(a.h.modelName=b.model),b.version&&(a.h.s=b.version),!a.l){var c=we();a.l=!0;a.h.g=tf(b.ip,c,a.D.bind(a))}}))};
ri.prototype.C=function(){this.g.logs=this.h.ae;this.g.logsHeader=Qg;this.g.sendLogs=Rg;this.g.fineLogsWarning=Sg;this.g.okButton=Tg;this.w.show({locals:{rK:this.g.attachLogs,ae:this.g.logs,FK:this.g.includeFineLogs,QK:this.g.logsHeader,bL:this.g.sendLogs,AK:this.g.fineLogsWarning,Rt:this.g.okButton},scope:this.g,preserveScope:!0,bindToController:!0,clickOutsideToClose:!0,template:'<md-dialog><md-dialog-content id="logs-dialog"><div class="subheading">{{logsHeader}}</div><div ng-show="includeFineLogs && attachLogs"id="feedback-fine-log-warning" class="informative">{{fineLogsWarning}}</div><pre>{{logs}}</pre><div class="send-logs"><md-checkbox type="checkbox" ng-model="attachLogs"ng-change="attachLogsClick()"><span>{{sendLogs}}</span></md-checkbox></div><md-dialog-actions><md-button class="md-raised md-primary"ng-click="closeDialog()">{{okButton}}</md-button></md-dialog-actions></md-dialog-content></md-dialog>',
controller:this.j})};ri.prototype.D=function(a,b){this.l=!1;this.h.g="error"==a?"":b;this.g.attachLogs||(this.h.g="");qi(this)};var qi=function(a){a.g.$$phase||a.g.$apply()};ri.prototype.j=function(a,b){a.closeWindow=function(){window.close()};a.closeDialog=function(){b.hide()}};ri.prototype.j.$inject=["$scope","$mdDialog"];var si=function(a,b){this.id=a;this.desc=b;this.text=0==a?b:a+" ("+b+")"};
angular.module("feedbackApp","chrome_18n material.components.button material.components.checkbox material.components.dialog material.components.input material.components.radioButton".split(" ")).controller("FeedbackCtrl",["$scope","$mdDialog",ri]);x("ng.safehtml.googSceHelper.isGoogHtmlType",function(a){return a&&a.fd?!0:!1});x("ng.safehtml.googSceHelper.isCOMPILED",function(){return!0});x("ng.safehtml.googSceHelper.unwrapAny",function(a){if(a instanceof bd)return cd(a).toString();if(a instanceof he)return ie(a).toString();if(a instanceof yd)return zd(a);if(a instanceof Dd)return Ed(a);if(a instanceof Tc)return Uc(a).toString();throw Error();});
x("ng.safehtml.googSceHelper.unwrapGivenContext",function(a,b){if("html"==a)return ie(b).toString();if("resourceUrl"==a||"templateUrl"==a)return cd(b).toString();if("url"==a)return b instanceof bd?cd(b).toString():zd(b);if("css"==a)return Ed(b);if("js"==a)return Uc(b).toString();throw Error();});