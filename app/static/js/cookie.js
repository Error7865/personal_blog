/**This file have cookie class which help to retrive or 
 * set cookies
 */

class Cookie{
    constructor(){
        let cookieStr=document.cookie
        let arr=cookieStr.split(';')
        this.data={}    
        let key, value
        for(let i=0;i<arr.length;i++){
            key=arr[i].split('=')[0]
            value=arr[i].split('=')[1]
            this.data[key]=value
        }
    }
    print(key){
        console.log(this.data)
    }
}