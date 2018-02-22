$(document).ready(function () {
    loadBaseURL();
    viewCatList();
    viewPosts();

    $("#search").on("keyup", function () {
        search($(this).val())
    });


    $(document).on('click', '.post-image', function () {
        post_id = $(this).attr('post-no');
        $.ajax({
            url: 'http://127.0.0.1:8000/posts/' + post_id + '/',
            type: 'get',
            success: function (response) {
                data = JSON.parse(response);
                modals = $('#modals_container');
                modals.html("");
                $(data).each(function () {
                    modals.append(postModal(this));
                    getComments(this.pk);
                });
                $('#postModal').modal('toggle');
            }
        });

    });
    $(document).on('click', '.sreachel', function () {
        post_id = $(this).attr('post-no');
        $.ajax({
            url: 'http://127.0.0.1:8000/posts/' + post_id + '/',
            type: 'get',
            success: function (response) {
                data = JSON.parse(response);
                modals = $('#modals_container');
                modals.html("");
                $(data).each(function () {
                    modals.append(postModal(this));
                    getComments(this.pk);
                });
                $('#postModal').modal('toggle');
            }
        });

    });
    $(document).on('click', '.category', function () {
        cat_name = $(this).html();
        if ($(this).attr('val') === '0')
            URL = 'http://127.0.0.1:8000/allPosts';
        else
            URL = 'http://127.0.0.1:8000/allCats/' + cat_name + '/';
        $.ajax({
            url: URL,
            type: 'get',
            success: function (response) {
                data = JSON.parse(response);
                posts = $('#posts');
                posts.html("");
                $(data).each(function () {
                    posts.append(post(this));
                });

            }
        });
    });
    $(document).on('click', '.sup', function (e) {
        self = this;
        cat_id = $(this).attr('data');
        //TODO dontforget to fix it #bug_1
        user_id = 1;
        $.ajax({
            url: 'http://127.0.0.1:8000/sup/' + cat_id + '/',
            type: 'get',
            success: function (response) {
                if (response)
                    toggle_btn(self)

            }
        });
    });
    $(document).on('click', '.unsup', function (e) {
        self = this;
        cat_id = $(this).attr('data');
        //TODO dontforget to fix it #bug_1
        $.ajax({
            url: 'http://127.0.0.1:8000/unsup/' + cat_id + '/',
            type: 'get',
            success: function (response) {
                if (response)
                    toggle_btn(self)

            }
        });
    });
    $(document).on('click', '.cat_trigger', function () {
        setActiveMenuItem('.cat_trigger', this);
    });
    $(document).on('click', '.cat_trigger', function () {
        setActiveMenuItem('.cat_trigger', this);
    });
    /*
    $(document).on('click', '.CommentButton', function() {
          modals = $('#addComments_modal');
          modals.html("");
          modals.append(CommentModal());
          $('#commentModal').modal('toggle');

        });
        */
    $(document).on('click', '.commentForm', function (e) {
        e.preventDefault();
        text = $('.CommentText').val();
        postNo = $('.post-image').attr('post-no');
        $.ajax({
            url: 'http://127.0.0.1:8000/addcomment/' + text + '/' + postNo,
            type: 'get',
            //data: {text: $('.CommentText').val()},
            success: function (response) {
                data = JSON.parse(response)[0];
                $('#comments').prepend(comments(data));
            }
        });
    });

    function br() {
        return $("<br>")
    }

    function category(data) {
        cat = JSON.parse(data.cat)[0]
        console.log(data)
        sup = "";
        if (userState()) {
            if (data.state)
                sup = '<button class="sup btn-outline-danger" data="' + cat.pk + '">Unsup</button>';
            else
                sup = '<button class="sup btn-outline-primary" data="' + cat.pk + '">Sup</button>';
        }

        return $('<span class="cat_trigger list-group-item category" val="' + cat.pk + '" >' + cat.fields.cat_name + '</span> ' + sup)
    }


    function cat_all() {
        return $('<span class="cat_trigger list-group-item active category " val="0">All </span>');
    }


    function post(data) {
        categorySpan = $('<span></span>');
        getCategory(data.fields.category, printCategoryname, categorySpan)
        post_div = $('  <div class="card mt-4">\n' +
            '            <img  post-no="' + data.pk + '" class="card-img-top img-fluid post-image"' +
            '               width="50px" height="50px" src="' + data.fields.picture + '"  alt="">\n' +
            '            <div class="card-body">\n' +
            '              <h3 class="card-title">' + data.fields.title + '</h3>\n' +
            '              <p class="card-text">' + data.fields.content + '</p>\n' +
            '              <p class="card-text">Category: <span class="postCat"></span></p>\n' +
            '            </div>\n' +
            '        </div>');
        post_div.find('.postCat').append(categorySpan);
        return post_div;
    }

    function setActiveMenuItem(item, activeItem) {
        $(item).each(function () {
            if (this === activeItem) {
                if (!$(this).hasClass("acctive"))
                    $(this).addClass("active");
            } else {
                $(this).removeClass("active");
            }
        });
    }

    function comments(data) {
        usernameSpan = $("<span></span>");
        replay = "";
        if (userState())
            replay = '<form method="get">' +
                '<textarea class="ReplyText"></textarea><br/>' +
                '<button class="btn btn-success replyForm">Leave a Reply</button> ' +
                '</form>';
        getUser(data.fields.username, printusername, usernameSpan);
        ret = $('<div class="card-body">\n' +
            '              <p>' + data.fields.text + '</p>\n' +
            '              <small class="text-muted">Commented by <span class="username"></span> on ' + data.fields.created_date + '</small>\n' +
            '<div>' +
            '<div comment-no="' + data.pk + '">' + Replys(data.fields.post, data.pk) + '</div>' +
            '<div>' + replay +
            '</div>' +
            '</div>' +
            '              <hr>\n' +
            '            </div>');
        ret.find(".username").append(usernameSpan);
        return ret;
    }

    function getComments(post_id) {
        $.ajax({
            url: 'http://127.0.0.1:8000/comments/' + post_id + '/',
            type: 'get',
            success: function (response) {
                data = JSON.parse(response);
                $('#comments').html('');
                $(data).each(function () {
                    $('#comments').append(comments(this));
                });

            }
        });
    }


    function getUser(user_id, handle, element) {
        $.ajax({
            url: 'http://127.0.0.1:8000/user/' + user_id + '/',
            type: 'get',
            success: function (response) {
                data = JSON.parse(response)[0];
                handle(data, element);
            }
        });
    }

    function getCategory(cat_id, handle, element) {
        $.ajax({
            url: 'http://127.0.0.1:8000/category/' + cat_id + '/',
            type: 'get',
            success: function (response) {
                data = JSON.parse(response)[0];
                handle(data, element);
            }
        });
    }

    function printusername(userObject, element) {
        $(element).append(data.fields.username);
    }

    function printCategoryname(catObject, element) {
        $(element).append(data.fields.cat_name)
    }

    function postModal(data) {
        like = "";
        comment = "";
        if (userState()) {
            like = '<div class="card-body">' +
                '<button class="btn-success like" post-no="' + data.pk + '">Like</button><input id="likeCounter" disabled />' +
                '<button class="btn-danger dislike"  post-no="' + data.pk + '">DisLike</button><input id="dislikeCounter" disabled/>' +
                '</div>';
            comment = '<div class="modal-body" id="FormContiner">\n' +
                '<form  method="get">' +
                '<textarea class="CommentText"></textarea><br/>' +
                '<button class="btn btn-success commentForm">Leave a Comment</button> ' +
                '</form>' +
                '            </div>\n';
        }
        ret = $('<div class="modal fade" id="postModal" tabindex="-1" role="dialog" aria-labelledby="Cart" aria-hidden="true">\n' +
            '    <div class="modal-dialog modal-lg" role="document">\n' +
            '        <div class="modal-content">\n' +
            '            <div class="modal-header">\n' +
            '                <h5 class="modal-title" id="exampleModalLabel">' + data.fields.title + '</h5>\n' +
            '                <button type="button" class="close" data-dismiss="modal" aria-label="Close">\n' +
            '                    <span aria-hidden="true">&times;</span>\n' +
            '                </button>\n' +
            '            </div>\n' +
            '            <div class="modal-body" id="postContiner">\n' +
            '            </div>\n' + like +
            '            <div><div class="card-header">' +
            '              Post Comments </div>' +
            '            <div class="modal-body" id="FormContiner">\n' +
            '            </div>\n' + comment +
            '               <div  id="comments"></div>' +
            '             </div>' +
            '        </div>\n' +
            '    </div>\n' +
            '</div>');
        ret.find("#postContiner").append(post(data));
        return ret;
    }

    function toggle_btn(btn) {
        if ($(btn).html() == "Sup")
            $(btn).html("Unsup")
        else
            $(btn).html("Sup")
        $(btn).toggleClass("btn-outline-primary")
        $(btn).toggleClass("btn-outline-danger")
        $(btn).toggleClass("sup")
        $(btn).toggleClass("unsup")
    }

    function Replys(post_id, comment_id) {
        $.ajax({
            url: 'http://127.0.0.1:8000/reply/' + post_id + '/' + comment_id,
            type: 'get',
            success: function (response) {
                data = JSON.parse(response);
                replydiv = $('div[comment-no="' + comment_id + '"]');
                replydiv.html('');
                $(data).each(function () {
                    replydiv.append(ReplyTemplate(this));

                });
            }
        });
    }

    function ReplyTemplate(data) {
        if (data === undefined || data === null) {
            ret = $('<div class="modal-body" >\n' +
                '             </div>');

        }
        else {
            usernameSpan = $("<span></span>");
            getUser(data.fields.username, printusername, usernameSpan);
            ret = $('               <div  class="modal-body" id="reply">' + data.fields.text +
                ' <br/><small class="text-muted">by <span class="username"></span> on ' + data.fields.created_date + '</small>' +
                '             </div>');
            ret.find(".username").append(usernameSpan);
        }
        return ret;

    }

    $(document).on('click', '.replyForm', function (e) {
        e.preventDefault();
        comment = $(this).parents()[2];
        commentNo = $(comment).find('div:first-child').attr('comment-no');
        text = $(comment).find('.ReplyText').val();
        postNo = $('.post-image').attr('post-no');
        $.ajax({
            url: 'http://127.0.0.1:8000/addreply/' + text + '/' + postNo + '/' + commentNo,
            type: 'get',
            success: function (response) {
                data = JSON.parse(response)[0];
                replydiv = $('div[comment-no="' + commentNo + '"]');
                replydiv.prepend(ReplyTemplate(data));
            }
        });
    });

    function searchRes(data) {
        return $('<li class="sreachel" post-no="' + data.pk + '">\n' +
            '\n' + data.fields.title +
            '    </li>');
    }

    function getLikes(post_id) {
        $.ajax({
            url: 'http://127.0.0.1:8000/likes/' + post_id + '/',
            type: 'get',
            success: function (response) {
                $('#likeCounter').val(response);
            }
        });
    }

    $(document).on('click', '.like', function (e) {
        e.preventDefault();
        post_id = $(this).attr('post-no');
        $.ajax({
            url: 'http://127.0.0.1:8000/addlike/' + post_id + '/',
            type: 'get',
            success: function (response) {
                getLikes(post_id);
            }
        });

    });
    $(document).on('click', '.dislike', function (e) {
        e.preventDefault();
        post_id = $(this).attr('post-no');
        $.ajax({
            url: 'http://127.0.0.1:8000/adddislike/' + post_id + '/',
            type: 'get',
            success: function (response) {
                if (response == 'deletePost') {
                    $('#postModal').modal('toggle');
                    viewPosts();
                    getDislikes(post_id);
                }
                else {
                    getDislikes(post_id);
                }
            }
        });

    });

    function getDislikes(post_id) {
        $.ajax({
            url: 'http://127.0.0.1:8000/dislikes/' + post_id + '/',
            type: 'get',
            success: function (response) {
                $('#dislikeCounter').val(response);
            }
        });

    }

    function userState() {
        return $("#userstate").attr("state") == "True" ? true : false;
    }

    function viewCatList() {
        $.ajax({
            url: 'http://127.0.0.1:8000/allCats',
            type: 'get',
            success: function (response) {
                data = JSON.parse(response);
                cats = $("#cats");
                cats.html("");
                cats.append(cat_all())
                $(data).each(function () {
                    cats.append(category(this));
                });
            }
        });
    }

    function search(term) {
        $.ajax({
            url: 'http://127.0.0.1:8000/search/' + term,
            type: 'get',
            success: function (response) {
                data = JSON.parse(response);
                cats = $("#searchRes");
                cats.html("");
                $(data).each(function () {
                    cats.append(searchRes(this));
                });
            }
        });
    }

    function loadBaseURL() {

        $.ajax({
            url: 'http://127.0.0.1:8000/base/',
            type: 'get',
            success: function (response) {

                baseurl = response.base_dir;
                $("#baseurl").html(baseurl);

            }
        });
    }

    function viewPosts() {
        $.ajax({
            url: 'http://127.0.0.1:8000/allPosts',
            type: 'get',
            success: function (response) {
                data = JSON.parse(response);
                posts = $('#posts');
                posts.html("");
                $(data).each(function () {
                    posts.append(post(this));
                });

            }
        });
    }

});


