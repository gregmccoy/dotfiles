set runtimepath+=~/.vim_runtime
set number

source ~/.vim_runtime/vimrcs/basic.vim
source ~/.vim_runtime/vimrcs/filetypes.vim
source ~/.vim_runtime/vimrcs/plugins_config.vim
source ~/.vim_runtime/vimrcs/extended.vim

highlight Normal ctermfg=grey ctermbg=black

try
source ~/.vim_runtime/my_configs.vim
catch
endtry
