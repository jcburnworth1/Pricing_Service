## Import libraries
import functools
from typing import Callable
from flask import session, flash, redirect, url_for, current_app

## Decorators
def requires_login(f: Callable) -> Callable:
    @functools.wraps(f) ## Pull original name and documentation into decorator
    def decorated_function(*args, **kwargs): ## Take any number of arguments / keyword arguments
        if not session.get('email'):
            flash('You need to be signed in for this page.', 'danger') ## Insert into a message queue
            return redirect(url_for('users.login_user'))
        return f(*args, **kwargs)
    return decorated_function

def requires_admin(f: callable) -> Callable:
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):  ## Take any number of arguments / keyword arguments
        if session.get('email') != current_app.config.get('ADMIN', ''):
            flash('You need to be an administrator to access this page.', 'danger')
            return redirect(url_for('users.login_user'))
        return f(*args, **kwargs)
    return decorated_function