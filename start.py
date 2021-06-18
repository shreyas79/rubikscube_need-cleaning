def check_cannonical(cube,ideal_cube):
    """This checks if the given cube is already in cannonical form, if not it makes the cube into cannonical form 
    by taking the ideal cube which contains list of lists, representing the ideal faces of the cube in a solved state"""
    col=['y','o','b','w','r','g']
    org_col =set(col)
    #check if length of ideal cube is 6, in that case it has 6 different images 
    if(len(ideal_cube)==6):
        dicti={}
        l=[]
        #check the number of colors that are required to make a single ideal face
        for i in range(len(cube)):
            for j in range(len (cube[i])):
                cube[i][j] =cube[i][j].lower()
                if(cube[i][j] in dicti):
                    dicti[cube[i][j]]+=1
                else:
                    dicti[cube[i][j]]=1
                    l.append(cube[i][j])
        ll=set(l)
        print(dicti)
        for a,b in dicti.items():
            if(b>9):
                print("error more than 9 instances of a color")
                return 
            
        #if the number of colors is 6, then it is almost similar to the original cannonical form, and can be formed 
        #with or without replacement of few colors
        if(len(dicti)==6):
            #if it is in cannonical form return the cube
            if(ll==org_col):
                return cube
            idx=0
            cur_col={}
            #if the colors in the cube dosent match the cannonical colors, mapp and replace the colors and return 
            for i in range(len(cube)):
                for j in range(len(cube[i])):
                    temp=cube[i][j]
                    if(temp in cur_col):
                        cube[i][j]=cur_col[temp]
                    else:
                        cur_col[temp]=col[idx]
                        idx+=1
                        cube[i][j]=cur_col[temp]
            return cube
        else:
            #if the number of colors in an ideal face is more than 1, then map the colors to a single color
            mapping={}
            idx=0
            for i in range(len(ideal_cube)):
                #map all the colors in a single ideal face to a single color
                for j in range(len(ideal_cube[i])):
                    temp=ideal_cube[i][j]
                    mapping[temp]=col[idx]
                idx+=1
            print(mapping)
            for i in range(len(cube)):
                for j in range(len(cube[i])):
                    cube[i][j]=mapping[cube[i][j]]
            return cube

    else:
        if(0<len(ideal_cube)<=3):
                    col_mapping={}
                    col_list=[]
                    count = 6//len(ideal_cube)
                    temp=[]
                    for i in range(len(col)):
                        temp.append(col[i])
                        if(len(temp)==count):
                            col_list.append(temp)
                            temp=[]
                    idx=-1
                    for i in range(len(ideal_cube)):
                        idx+=1

                        for j in range(len(ideal_cube[i])):

                            temp=ideal_cube[i][j]
                            if(temp in col_mapping):
                                continue
                            else:

                                col_mapping[temp]=deepcopy(col_list[idx])
                    for i in range(len(cube)):
                        for j in range(len(cube[i])):
                            temp=col_mapping[str(cube[i][j])]
                            cube[i][j]=temp.pop()
                            print(col_mapping)
                    
                    
            
        else:
            print("error not possible mapping")
            return False



def get_result(cube):
    color_count={}
    for i in range(len(cube)):
        temp_dict={}
        for j in range(len(cube[i])):
            temp=cube[i][j]
            if(temp in temp_dict):
                temp_dict[temp]+=1
            else:
                temp_dict[temp]=1
        for a,b in temp_dict.items():
            if(a in color_count):
                color_count[a].append(str(b))
            else:
                color_count[a]=[str(b)]
    hash = set()
    for i,j in color_count.items():
        hash.add("".join(j))
    res = get_key(hash)
    for i in res:
        if(check(cube,i)):
            return True
    return False


def check(res,res2):
    vis=[]
    mapping={}
    mid=len(res[0])//2
    from copy import deepcopy
    for i in range(len(res)):
        for j in range(len(res2)):
            temp_mapping=deepcopy(mapping)
            if(j in vis):
                continue
            temp = res[i][mid]
            if(temp in temp_mapping):
                if(temp_mapping[temp]!=res2[j][mid]):
                    continue
            else:
                temp_mapping[temp]=res2[j][mid]
            idx=0
            while(idx<len(res)):
                if(res[i][idx] in temp_mapping):
                    if(temp_mapping[res[i][idx]]!=res2[j][idx]):
                        break
                else:
                    temp_mapping[res[i][idx]]=res2[j][idx]
                idx+=1
            else:
                mapping=deepcopy(temp_mapping)
                vis.append(j)
    print(mapping)
    if(len(mapping)==6):
        return True
    return False





    

















def get_key(hash):
    """this function in actuality will get records which as the @hash as the key, a basic first line of check"""
    pass









    