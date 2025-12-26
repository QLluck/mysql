// 公共JavaScript函数

// 显示提示信息
function showAlert(message, type = 'info') {
    const alertHtml = `
        <div class="alert alert-${type} alert-dismissible fade show" role="alert">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
    $('#alert-container').html(alertHtml);
    
    // 3秒后自动关闭
    setTimeout(() => {
        $('.alert').alert('close');
    }, 3000);
}

// 确认对话框
function confirmAction(message, callback) {
    if (confirm(message)) {
        callback();
    }
}

// 发送API请求
function apiRequest(url, method, data, successCallback, errorCallback) {
    $.ajax({
        url: url,
        method: method,
        contentType: 'application/json',
        data: data ? JSON.stringify(data) : null,
        success: function(response) {
            if (response.success) {
                if (successCallback) successCallback(response);
            } else {
                showAlert(response.message || '操作失败', 'danger');
                if (errorCallback) errorCallback(response);
            }
        },
        error: function(xhr) {
            const message = xhr.responseJSON?.message || '网络错误';
            showAlert(message, 'danger');
            if (errorCallback) errorCallback(xhr);
        }
    });
}

// 格式化日期时间
function formatDateTime(dateString) {
    if (!dateString) return '-';
    const date = new Date(dateString);
    return date.toLocaleString('zh-CN');
}

// 退出登录
function logout() {
    apiRequest('/api/logout', 'POST', null, function() {
        window.location.href = '/login.html';
    });
}

