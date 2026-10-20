import {readdir,readFile,stat,rm,cp} from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const source=path.join(root,'dist'),output=path.join(root,'build');
async function walk(dir){let all=[];for(const entry of await readdir(dir,{withFileTypes:true})){const f=path.join(dir,entry.name);all.push(...(entry.isDirectory()?await walk(f):[f]));}return all;}
const files=await walk(source),errors=[];let pages=0;
for(const file of files){if(file.endsWith('.html')){pages++;const html=await readFile(file,'utf8');for(const match of html.matchAll(/(?:href|src)=["']([^"']+)["']/g)){const link=match[1];if(/^(?:[a-z]+:|#|\/\/)/i.test(link))continue;const url=new URL(link,'https://local.invalid/'+path.relative(source,file).split(path.sep).join('/'));let local=path.join(source,decodeURIComponent(url.pathname));try{if((await stat(local)).isDirectory())local=path.join(local,'index.html');await stat(local);}catch{errors.push(path.relative(source,file)+': '+link);}}}}
for(const file of files.filter(f=>f.endsWith('.js')||f.endsWith('.mjs'))){const check=spawnSync(process.execPath,['--check',file],{encoding:'utf8'});if(check.status!==0)errors.push(check.stderr);}
if(errors.length){console.error(errors.join('\n'));process.exit(1);}
await rm(output,{recursive:true,force:true});await cp(source,output,{recursive:true});
console.log(`Built ${pages} pages and ${files.length-pages} supporting files into build/. All local HTML references and JavaScript syntax checks passed.`);
