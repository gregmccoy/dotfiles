set runtimepath+=~/.vim_runtime
set number

source ~/.vim_runtime/vimrcs/basic.vim
source ~/.vim_runtime/vimrcs/filetypes.vim
source ~/.vim_runtime/vimrcs/plugins_config.vim
source ~/.vim_runtime/vimrcs/extended.vim

"Background Colour
highlight Normal ctermfg=grey ctermbg=black

"Bracket highlight colour
highlight MatchParen cterm=bold ctermbg=black ctermfg=green

:nnoremap <silent> [<space> :pu! _<cr>:']+1<cr>
:nnoremap <silent> ]<space> :pu _<cr>:'[-1<cr>
try
source ~/.vim_runtime/my_configs.vim
catch
endtry
