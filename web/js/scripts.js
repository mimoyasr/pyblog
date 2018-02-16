$.ajax({
            url: 'http://127.0.0.1:8000/allCats',
            type: 'get',
            success: function (response) {
                data = JSON.parse(response);
                cats = $("#cats");
                cats.html("");
                cats.append(cat_all())
                $(data).each(function(){
                    cats.append(category(this));
                });
            }
        });

$.ajax({
            url: 'http://127.0.0.1:8000/allPosts',
            type: 'get',
            success: function (response) {
                data = JSON.parse(response);
                console.log(data)
                posts = $('#posts');
                posts.html("");
                $(data).each(function(){
                    posts.append(post(this));
                });

            }
        });


$(document).on('click', '.cat_trigger', function() {
       setActiveMenuItem('.cat_trigger',this);
       console.log($(this).attr("val"))
    });

function br() {
    return $("<br>")
}

function category(cat) {
    console.log(cat);
    // <a href="#" class="list-group-item active">Category 1</a>
    return $('<a href="#" class="cat_trigger list-group-item " val="'+cat.pk+'" >'+cat.fields.cat_name+'</a>')
}


function cat_all() {
    return $('<a href="#" class="cat_trigger list-group-item active" val="0">All </a>');
}


function post(data) {
    return $('  <div class="card mt-4">\n' +
        '            <img class="card-img-top img-fluid" src="'+data.fields.picture+'" alt="">\n' +
        '            <div class="card-body">\n' +
        '              <h3 class="card-title">'+data.fields.title+'</h3>\n' +
        '              <p class="card-text">'+data.fields.content+'</p>\n' +
        '            </div>\n' +
        '          </div>' +
        '        </div>')
}

function setActiveMenuItem(item, activeItem) {
    $(item).each(function() {
        if (this === activeItem) {
            if (!$(this).hasClass("acctive"))
                $(this).addClass("active");
        } else {
            $(this).removeClass("active");
        }
    });
}