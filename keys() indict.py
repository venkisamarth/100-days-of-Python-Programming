# python keys() method is used to featch all the keys form the dic 

fees={"karna":12000,"jeson":3000,"john":1400}
keys_view=list(fees.keys())
print(keys_view)
print(type(keys_view))

fees={"karna":12000,"jeson":13000,"jeshon":14000}
act_fees=15000
keys_list=list(fees.keys())
for key in keys_list:
    print(f"student{key}has got discount of rs.",act_fees-fees[key])