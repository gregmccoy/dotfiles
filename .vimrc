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

"Pydocstring
let g:template_vim_template_dir = '~/.vim_runtime/docstring/'
let g:pydocstring_templates_dir = '/home/ubuntu/.vim_runtime/docstring/'

:nnoremap <silent> [<space> :pu! _<cr>:']+1<cr>
:nnoremap <silent> ]<space> :pu _<cr>:'[-1<cr>
try
source ~/.vim_runtime/my_configs.vim
catch
endtry

command Scom :normal i{% comment %}<ESC>
command Ecom :normal i{% endcomment %}<ESC>
