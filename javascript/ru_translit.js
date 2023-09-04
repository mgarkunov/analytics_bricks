function ru_translit(txt){
  txt = decodeURI(txt).replace("  ", " ").toLowerCase();
  var dict = {
    'а':'a',
    'б':'b',
    'в':'v',
    'г':'g',
    'д':'d',
    'е':'e',
    'ё':'e',
    'ж':'zh',
    'з':'z',
    'и':'i',
    'й':'i',
    'к':'k',
    'л':'l',
    'м':'m',
    'н':'n',
    'о':'o',
    'п':'p',
    'р':'r',
    'с':'s',
    'т':'t',
    'у':'u',
    'ф':'f',
    'х':'h',
    'ц':'c',
    'ч':'ch',
    'ш':'sh',
    'щ':'sch',
    'ъ':'',
    'ы':'y',
    'ь':'',
    'э':'e',
    'ю':'u',
    'я':'ya',
    ' ':'_',
    ':':'_',
    '-':'_',  
  };
  var out = "";
  for (var w = 0; w < txt.length; w++){
    out += dict[txt[w]] != undefined ? dict[txt[w]] : txt[w];
  }
  return out;
}