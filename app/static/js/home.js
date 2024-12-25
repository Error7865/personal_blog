$(document).ready((e)=>{
    // main 
    switchImgTab()
    $('.arrow-container').on('click', (e)=>{
        styleArrowCon()
    })
    // attach click event for close form part 
    $('.close').on('click', (e)=>{
        $('#hide').val('')
        $('#art_title').val('')
        $('#desc').val('')
        styleLeft(rev=true)
        styleArrowCon(rev=true)
    })

    $('.ls-art').on('click', (e)=>{
        let target = $(e.target)
        document.querySelector('.arrow-container').click()
        post_data('/open/artinfo', {id: target.data('id')}, (data)=>{
            $('#hide').val(target.data('id'))
            $('#art_title').val(data.title)
            $('#desc').val(data.markdown)
        })
    })
})

function switchImgTab() {
    /**This function will swith image tab by opening and 
     * closing base on .con display value
     */

    $('.admin-info-holder').on('click', openTab)
    $('.cross').on('click', closeTab)
}
function openTab(){
    /* enable image tab */
    var con=$('.con')
    console.log('here ', con.css('display'));
    if(con.css('display') == 'none'){
        //show con
        con.css({'display': 'block'})
        setTimeout(()=>{
            con.css('opacity', 1)
        }, 200)
    }
}

function closeTab(){
    /**close image tab */
    $('.con').css('opacity', 0)
    setTimeout(()=>{
        $('.con').css('display', 'none')
    }, 500)
}

function styleArrowCon(rev=false){
    /**This will help to style .arrow-container div */
    let arrow=$('.arrow-container')
    defaultSize='60px'
    if(!rev){arrow.css('width')=='60px'
        arrow.css('width', '10px')
        setTimeout(()=>{
            arrow.css('display', 'none')
            styleLeft()
        }, 600)
    }else{
        arrow.css('display', 'flex')
        setTimeout(()=>{
            // styleLeft(rev=true)
            arrow.css('width', '60px')
        }, 400)
    }
}

function styleLeft(rev=false){
    /**This function will expan & shrink .left element
     * width
     */
    let el=$('.left')
    if(!rev){
        el.css('display', 'flex')
        setTimeout(()=>{
            el.css('width', '100vw')
        }, 200)
    }
    // return el.css('width', '0')
    else{
        el.css('width', '0')
        setTimeout(()=>{
            el.css('display', 'none')
        }, 500)
    }
}

function post_data(url, data, success) {
    $.ajax({
        type: 'POST', 
        url: url,
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(data),
        success: success
    })
}
