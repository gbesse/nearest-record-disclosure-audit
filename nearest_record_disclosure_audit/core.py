from .common import number,unique_ids

def run(data):
 fields=data['fields'];source=data['source'];holdout=data['holdout'];synthetic=data['synthetic']
 if not isinstance(fields,dict)or not 1<=len(fields)<=30 or max(len(source),len(holdout),len(synthetic))>1000 or len(synthetic)*(len(source)+len(holdout))*len(fields)>1000000:raise ValueError('bounds')
 for rows in(source,holdout,synthetic):unique_ids(rows)
 if {x['id']for x in source}&{x['id']for x in holdout}:raise ValueError('source_holdout_id_overlap')
 for key,f in fields.items():
  if f['kind']=='numeric':number(f['minimum']);number(f['maximum'],f['minimum'])
  elif f['kind']!='category':raise ValueError('kind')
 for row in source+holdout+synthetic:
  for key,f in fields.items():
   v=row.get(key)
   if v is None:continue
   if f['kind']=='numeric':number(v,f['minimum'],f['maximum'])
   elif not isinstance(v,str):raise ValueError('category')
 def distance(a,b):
  parts=[]
  for key,f in fields.items():
   x=a.get(key);y=b.get(key)
   if x is None or y is None:continue
   if f['kind']=='category':parts.append(float(x!=y))
   else:
    width=f['maximum']-f['minimum'];parts.append(abs(x-y)/width if width else 0)
  return sum(parts)/len(parts)if parts else None
 def nearest(row,pool):
  candidates=[(distance(row,x),x['id'])for x in pool];candidates=[x for x in candidates if x[0]is not None]
  if not candidates:return None
  d,name=min(candidates);return {'id':name,'distance':d}
 out=[]
 for row in synthetic:
  a=nearest(row,source);b=nearest(row,holdout);out.append({'synthetic_id':row['id'],'nearest_source':a,'nearest_holdout':b,'closer_to_source':a['distance']<b['distance']if a and b else None})
 return {'records':out,'model':'exact_declared_range_gower_nearest_record_diagnostic_not_privacy_certificate'}
