(provide "ruby" "3.1.2")

(when-let ((ruby-root (env/get "RUBY_ROOT")))
 (env/remove-from-pathlist "PATH" (path-concat ruby-root "bin"))
 (when-let ((gem-root (env/get "GEM_ROOT")))
   (env/remove-from-pathlist "PATH" (path-concat gem-root "bin")))
 (when-let ((gem-home (env/get "GEM_HOME")))
   (env/remove-from-pathlist "PATH" (path-concat gem-home "bin"))))

(env/set "BUNDLE_PATH" ())
(env/set "GEM_PATH" ())
(env/set "GEM_HOME" ())
(env/set "RUBYOPT" ())
(env/set "RUBYLIB" ())

(env/set "RUBY_ROOT" "/opt/rubies/3.1.2")
(env/prepend-to-pathlist "PATH" "/opt/rubies/3.1.2/bin")
(env/set "RUBY_ENGINE" "ruby")
(env/set "RUBY_VERSION" "3.1.2")
(env/set "GEM_ROOT" "/opt/rubies/3.1.2/lib/ruby/gems/3.1.0")

(when-let ((gem-root (env/get "GEM_ROOT")))
  (env/prepend-to-pathlist "GEM_PATH" gem-root)
  (env/prepend-to-pathlist "PATH" (path-concat gem-root "bin")))

(let ((gem-home
      (path-concat (env/get "HOME") ".gem" (env/get "RUBY_ENGINE") (env/get "RUBY_VERSION"))))
  (do
    (env/set "GEM_HOME" gem-home)
    (env/prepend-to-pathlist "GEM_PATH" gem-home)
    (env/prepend-to-pathlist "PATH" (path-concat gem-home "bin"))))

; See rails/rails#38560, typhoeus/typhoeus#687, typhoeus/ethon#206
(env/set "OBJC_DISABLE_INITIALIZE_FORK_SAFETY" "YES")
