(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[75],{222:function(n,I,_){!function(n){"use strict";n.defineMode("ntriples",(function(){var n={PRE_SUBJECT:0,WRITING_SUB_URI:1,WRITING_BNODE_URI:2,PRE_PRED:3,WRITING_PRED_URI:4,PRE_OBJ:5,WRITING_OBJ_URI:6,WRITING_OBJ_BNODE:7,WRITING_OBJ_LITERAL:8,WRITING_LIT_LANG:9,WRITING_LIT_TYPE:10,POST_OBJ:11,ERROR:12};function I(I,_){var R,t=I.location;R=t==n.PRE_SUBJECT&&"<"==_?n.WRITING_SUB_URI:t==n.PRE_SUBJECT&&"_"==_?n.WRITING_BNODE_URI:t==n.PRE_PRED&&"<"==_?n.WRITING_PRED_URI:t==n.PRE_OBJ&&"<"==_?n.WRITING_OBJ_URI:t==n.PRE_OBJ&&"_"==_?n.WRITING_OBJ_BNODE:t==n.PRE_OBJ&&'"'==_?n.WRITING_OBJ_LITERAL:t==n.WRITING_SUB_URI&&">"==_||t==n.WRITING_BNODE_URI&&" "==_?n.PRE_PRED:t==n.WRITING_PRED_URI&&">"==_?n.PRE_OBJ:t==n.WRITING_OBJ_URI&&">"==_||t==n.WRITING_OBJ_BNODE&&" "==_||t==n.WRITING_OBJ_LITERAL&&'"'==_||t==n.WRITING_LIT_LANG&&" "==_||t==n.WRITING_LIT_TYPE&&">"==_?n.POST_OBJ:t==n.WRITING_OBJ_LITERAL&&"@"==_?n.WRITING_LIT_LANG:t==n.WRITING_OBJ_LITERAL&&"^"==_?n.WRITING_LIT_TYPE:" "!=_||t!=n.PRE_SUBJECT&&t!=n.PRE_PRED&&t!=n.PRE_OBJ&&t!=n.POST_OBJ?t==n.POST_OBJ&&"."==_?n.PRE_SUBJECT:n.ERROR:t,I.location=R}return{startState:function(){return{location:n.PRE_SUBJECT,uris:[],anchors:[],bnodes:[],langs:[],types:[]}},token:function(n,_){var R=n.next();if("<"==R){I(_,R);var t="";return n.eatWhile((function(n){return"#"!=n&&">"!=n&&(t+=n,!0)})),_.uris.push(t),n.match("#",!1)||(n.next(),I(_,">")),"variable"}if("#"==R){var e="";return n.eatWhile((function(n){return">"!=n&&" "!=n&&(e+=n,!0)})),_.anchors.push(e),"variable-2"}if(">"==R)return I(_,">"),"variable";if("_"==R){I(_,R);var r="";return n.eatWhile((function(n){return" "!=n&&(r+=n,!0)})),_.bnodes.push(r),n.next(),I(_," "),"builtin"}if('"'==R)return I(_,R),n.eatWhile((function(n){return'"'!=n})),n.next(),"@"!=n.peek()&&"^"!=n.peek()&&I(_,'"'),"string";if("@"==R){I(_,"@");var i="";return n.eatWhile((function(n){return" "!=n&&(i+=n,!0)})),_.langs.push(i),n.next(),I(_," "),"string-2"}if("^"==R){n.next(),I(_,"^");var T="";return n.eatWhile((function(n){return">"!=n&&(T+=n,!0)})),_.types.push(T),n.next(),I(_,">"),"variable"}" "==R&&I(_,R),"."==R&&I(_,R)}}})),n.defineMIME("application/n-triples","ntriples"),n.defineMIME("application/n-quads","ntriples"),n.defineMIME("text/n-triples","ntriples")}(_(47))}}]);
//# sourceMappingURL=75.b090e899.chunk.js.map