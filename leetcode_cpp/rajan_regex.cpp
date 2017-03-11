//
//  main.cpp
//  subString
//
//  Created by Rajankumar Singh on 8/20/16.
//  Copyright © 2016 Rajankumar Singh. All rights reserved.
//

#include <iostream>

enum Type
{
    star = 0,
    slashStar,
    character
};

Type type(std::string str, int index)
{
    if(str[index] == '*')
    {
        if( index - 1 == 0)
        {
            return star;
        }
        else if( index -1 >= 0)
        {
            if(str[index-1] == '\\')
               return slashStar;
            else
               return star;
        }
    }
    
    return character;
}

/* handling these cases
             str2 -->
 str1        character star  slashStar
 character
 star
 slashStar
 */

bool checkSubString(std::string str1, std::string str2)
{
    int len1 = str1.length()-1;
    int len2 = str2.length()-1;
    
    while(len1 && len2)
    {
        if(len1 < 0) return false;

        if(type(str2, len2) == character)
        {
            if(type(str1, len1) == character)
            {
                if( str1[len1] == str2[len2])
                    len2--;
                
                len1--;
            }
            else if(type(str1, len1) == star)
                return true;
            else if(type(str1, len1) == slashStar)
                len1-=2;
        }
        else if(type(str2, len2) == star)
        {
            if(type(str1, len1) == character)
                len2--;
            else if(type(str1, len1) == star)
                return true;
            else if(type(str1, len1) == slashStar)
                len2 -=2;
        }
        else if(type(str2, len2) == slashStar)
        {
            if(type(str1, len1) == character)
                len2-=2;
            else if(type(str1, len1) == star)
                return true;
            else if(type(str1, len1) == slashStar)
            {
                len2-=2;
                len1-=2;
            }
        }
        
        if(len2 == 0) return true;
    }
    
    return false;
    
}

int main(int argc, const char * argv[])
{
    std::string str1, str2;
    
    std::getline(std::cin, str1);
    std::getline(std::cin, str2);
    
    std::cout << (checkSubString(str1, str2) ? "true":"false") <<"\n";

    return 0;
}