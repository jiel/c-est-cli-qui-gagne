import{d as _,i as d,a as p,u,b as h,c as m,e as g,f as n,g as t,t as s,h as a,F as f,r as v,n as x,j as y,o as i,k as b,l as k,m as N,p as w,q as P,_ as S}from"./index-28d490cd.js";import{N as V}from"./NoteDisplay-f08d29bb.js";const j={class:"m-4"},L={class:"mb-10"},T={class:"text-4xl font-bold mt-2"},q={class:"opacity-50"},B={class:"text-lg"},C={class:"font-bold flex gap-2"},D={class:"opacity-50"},H=t("div",{class:"flex-auto"},null,-1),z={key:0,class:"border-gray-400/50 mb-8"},F=_({__name:"PresenterPrint",setup(M){d(p),u(`
@page {
  size: A4;
  margin-top: 1.5cm;
  margin-bottom: 1cm;
}
* {
  -webkit-print-color-adjust: exact;
}
html,
html body,
html #app,
html #page-root {
  height: auto;
  overflow: auto !important;
}
`),h({title:`Notes - ${m.title}`});const r=g(()=>y.slice(0,-1).map(o=>{var l;return(l=o.meta)==null?void 0:l.slide}).filter(o=>o!==void 0&&o.noteHTML!==""));return(o,l)=>(i(),n("div",{id:"page-root",style:x(a(P))},[t("div",j,[t("div",L,[t("h1",T,s(a(m).title),1),t("div",q,s(new Date().toLocaleString()),1)]),(i(!0),n(f,null,v(a(r),(e,c)=>(i(),n("div",{key:c,class:"flex flex-col gap-4 break-inside-avoid-page"},[t("div",null,[t("h2",B,[t("div",C,[t("div",D,s(e==null?void 0:e.no)+"/"+s(a(b)),1),k(" "+s(e==null?void 0:e.title)+" ",1),H])]),N(V,{"note-html":e.noteHTML,class:"max-w-full"},null,8,["note-html"])]),c<a(r).length-1?(i(),n("hr",z)):w("v-if",!0)]))),128))])],4))}}),R=S(F,[["__file","/home/runner/work/c-est-cli-qui-gagne/c-est-cli-qui-gagne/node_modules/@slidev/client/internals/PresenterPrint.vue"]]);export{R as default};
