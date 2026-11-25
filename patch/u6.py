import json,lzma,base64,re,sys,os
D="/Td6WFoAAATm1rRGAgAhARwAAAAQz1jM4AihA5ZdAD2Iigdj/BWdOWk/OOEq+kWIqn+iAOVAbd/UpscIPPHKUging/B/DocvjvFBe6BhXm/AjWDkzE7s7VBaooIbrvqAofoVqF658pSyWBjh1zbqwhfu7VGjjEmyv7ru6Hv/LXvhxfh1txL82XoD0PHP4PDpysK8mCviEjnuPJafo+upFisTqAeEmbXJu2GtL5uIc1vqeDEnDf86wUX2643h2JzdnDmyh/j6J0SNDCYACr3sXTvyzbkaA4G86HDQ90bNHrtyzLFCuOqjg/8crg87gnVRlxpz0rf5s2s1+7ChX9I5AiHmaOsxTZw/dnZ3ONY54/7gl5kQLc+crhvSvSVgJIhcB2BM89yyAZjXUYCTkj2MvBxT7Khox1+N34rTJVGfiduV+VMgsfucaHnYRT1+n8TQZf0JHk20lsQKENMStSZqqlokiiaPrgJBOZkGk5ElF5MkCunnWF1ONNOWvn0aDx8uvIJWdDx46GcOOEPVW6oowdV3Hxp4DGyirDFIXna1aKev1QAEf1lYaCotcY68rJFXP6BF2BNegwKOpfA9L4aOLe3ZXsEKP+0lYmKGSr1myzCv1lTFSiNEATNoCh2dGPVLDx5umvxd1ju7OXAKu/KwRar90eQSMwC8o2CAMwnvVeG317y3BCAFk8/vDk3WMbuKZI3Kw14dB4y161xrJmQX1+mlPjg/6pKSvH6a2h9GFsGR8a5p35WhMLIAZKWBOZlQh+u8QA5fLq7crJBHykpMK96vaJSSSCxMO8WpVJlM/zuTT8BO6aCPwMJGmPUt6/Zs8CYKVxcFgvEdZausR9KnWCM3/pzKq0DBDNFz3YjoQaSCCvRjooIhvJl8wwKyq6qHnk2hIpfZx06m2lGyvojXf5xKszKd88LK5ccmS0i8AH5157yr9q/86M1trFDXUNlw/8CiTG4SH/LHC6duFIpXMI9/b72rbEK67zGHm9TuAPutfre5Y8Vk3IC9KXH9BGUK/gfl49LpdM48ciN5/ECLgQQWkThPQKm2+6Vs3n3VF3kyvXiyP/w1yP4uovFegtf83SQFJqP5FsGQfoS+dbm60xaOzvwe0Z+8i31iZWE/Khe720MI2jhR/+HGJbVpHtlDUuBTeo/lt5a9k1DeQiBXyEMtDnFwWbIagUoST8gZbJ+zCM5fRacbvIhx9P1PaYbId+4mtETAB9L2iZ8aNvqwxpDJJ3uERBF4K03cvKuWIUovJ2NoAAAAAN/IofpwxQUdAAGyB6IRAAB6ovHcscRn+wIAAAAABFla"
d=sys.argv[1];ops=json.loads(lzma.decompress(base64.b64decode(D)))
tok=lambda s:re.split(r'(?<=[>;}\n])',s)
for f,o in ops.items():
  p=os.path.join(d,f)
  if o[0]=='new':
    open(p,'w',encoding='utf-8').write(o[1]);continue
  t=tok(open(p,encoding='utf-8').read());assert len(t)==o[1],(f,len(t),o[1])
  for i1,i2,rep in reversed(o[2]): t[i1:i2]=[rep]
  open(p,'w',encoding='utf-8').write(''.join(t))
print('u6 ok',len(ops))
